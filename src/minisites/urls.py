from rest_framework import routers
from django.urls import path, include
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.static import static
from django.views.generic import View

from minisites.views import (SiteHome, SiteSearch, SiteAid, SiteAlert,
                             SiteLegalMentions)


# This set of url patterns is completely independant from all other urls.
# The `normal` core url patterns is set in `core.settings` to `core.urls`
# This is a custom set of url patterns, set in `minisites.settings`.


router = routers.DefaultRouter()

api_patterns = [
    path('', include(router.urls)),
    path('perimeters/', include('geofr.api.urls')),
    path('backers/', include('backers.api.urls')),
]

urlpatterns = [

    # We give two names to the same view, because with minisites, the search
    # form is also the home page.
    path('', SiteHome.as_view(),  name='home'),
    path('', SiteHome.as_view(),  name='search_view'),

    # This is the full search form
    path(_('search/'), SiteSearch.as_view(), name='advanced_search_view'),

    # Minisite users must be able to create alerts
    path(_('alerts/'), include([
        path('', SiteAlert.as_view(), name='alert_create_view'),

        # We need to define this url so django can resolve it and generate a
        # token validation email. However, when the user clicks this link,
        # they will be sent to the regular site
        path(_('<slug:token>/validate/'), View.as_view(),
             name='alert_validate_view'),
    ])),

    path(_('legal-mentions/'), SiteLegalMentions.as_view(),
         name='legal_mentions'),

    # Api related routes
    path('api/', include(api_patterns)),

    # The aid detail view
    path('<slug:slug>/', include([
        path('', SiteAid.as_view(), name='aid_detail_view')])),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns = static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns
