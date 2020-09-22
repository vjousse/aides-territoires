from django.http import QueryDict, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.sites.models import Site

from search.models import SearchPage
from aids.views import SearchView, AdvancedSearchView, AidDetailView
from alerts.views import AlertCreate


class MinisiteMixin:
    """Common code for all minisite urls.

    For every minisite view, we need to fetch the actual SearchPage object and
    inject it into the template.

    Note: there are several ways access the search page, hence there are
    several ways to access the SearchPage slug.

     1/ https://aides-territoires.beta.gouv.fr/recherche/<partner>/
     2/ https://<partner>.aides-territoires.beta.gouv.fr/
     3/ https://aides.<partner>.com (completely custom domain)

    In the fist case, we get the SearchPage's slug from the url parameter;
    Second case, from the subdomain;
    Third case, it is passed by a custom http header set in Nginx's settings.
    """

    def get(self, request, *args, **kwargs):
        self.search_page = self.get_search_page()

        if self.search_page is None:
            # Here, we have a bit of a problem.
            # If the SearchPage object is not found, we can't display a 404
            # error, because the 404 template needs a SearchPage to be
            # displayed.
            # Hence, the best way is to redirect to a sensible url.
            # Those errors are mainly caused by very old links with invalid
            # urls existing in the wild,
            # e.g https://www.aides-territoires.beta.gouv.fr
            return HttpResponseRedirect(self.get_redirection_url())

        return super().get(request, *args, **kwargs)

    def get_redirection_url(self):
        """What url to redirect to in case of missing SearchPage object.

        For now, just redirect to the main site's homepage.
        """
        site = Site.objects.get_current()
        url = 'https://{domain}'.format(domain=site.domain)
        return url

    def get_search_page(self):
        """Get the custom page from url."""

        HEADER = 'X-Minisite-Name'

        if 'search_slug' in self.kwargs:
            page_slug = self.kwargs.get('search_slug')
        elif HEADER in self.request.headers:
            page_slug = self.request.headers[HEADER]
        else:
            host = self.request.get_host()
            page_slug = host.split('.')[0]

        qs = SearchPage.objects.filter(slug=page_slug)
        try:
            obj = qs.get()
        except qs.model.DoesNotExist:
            obj = None
        return obj

    def get_context_data(self, **kwargs):

        # Canonical url definition
        # E.g we want to mark `aides.francemobilites.fr` as a duplicate of
        # `francemobilites.aides-territoires.beta.gouv.fr`.
        main_site_domain = Site.objects.get_current().domain
        page_subdomain = self.search_page.slug
        canonical_url = f'https://{page_subdomain}.{main_site_domain}'

        context = super().get_context_data(**kwargs)
        context['search_page'] = self.search_page
        context['site_url'] = self.request.build_absolute_uri('').rstrip('/')
        context['canonical_url'] = canonical_url

        return context


class SiteHome(MinisiteMixin, SearchView):
    """A static search page with admin-customizable content."""

    template_name = 'minisites/search_page.html'

    def get_form_kwargs(self):
        """Set the data passed to the form.

        If no data was provided by the user, then we use the initial
        querystring provided by admins.

        If the form was submitted, the GET values are set, we use those
        instead.
        """
        initial_data = QueryDict(
            self.search_page.search_querystring, mutable=True)
        user_data = self.request.GET.copy()
        user_data.pop('page', None)
        user_data.pop('integration', None)
        data = user_data or initial_data
        kwargs = super().get_form_kwargs()
        kwargs['data'] = data

        # XXX Ici, ne pas passer les données GET en `data` du formulaire.
        # Seulement pour les champs audiance et categories
        return kwargs

    def get_form(self, form_class=None):
        """Returns the aid search and filter form.

        The minisite feature allows admin to filter the available values for
        some filters (audiences and categories).
        """
        form = super().get_form(form_class)

        # Only show available values in categories filter field
        available_categories = self.search_page \
            .available_categories \
            .select_related('theme')
        if available_categories:
            form.fields['categories'].queryset = available_categories

        # Only show available values in the targeted audience filter field
        if self.search_page.available_audiences:
            all_audiences = form.fields['targeted_audiences'].choices
            available_audiences = self.search_page.available_audiences
            filtered_audiences = [
                audience for audience in all_audiences
                if audience[0] in available_audiences
            ]
            form.fields['targeted_audiences'].choices = filtered_audiences

        return form


class SiteSearch(MinisiteMixin, AdvancedSearchView):
    """The full search form."""

    template_name = 'minisites/advanced_search.html'


class SiteAid(MinisiteMixin, AidDetailView):
    """The detail page of a single aid."""

    template_name = 'minisites/aid_detail.html'


class SiteAlert(MinisiteMixin, AlertCreate):
    pass


class SiteLegalMentions(MinisiteMixin, TemplateView):
    template_name = 'minisites/legal_mentions.html'


class Error(MinisiteMixin, TemplateView):
    template_name = 'minisites/404.html'
    status_code = 404

    def render_to_response(self, context, **response_kwargs):
        response_kwargs['status'] = self.status_code
        return super().render_to_response(context, **response_kwargs)
