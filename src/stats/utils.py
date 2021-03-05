from core.celery import app
from core.utils import get_subdomain_from_host
from search.utils import (
    clean_search_querystring,
    get_querystring_value_from_key, get_querystring_value_list_from_key,
    get_querystring_perimeter,
    get_querystring_themes, get_querystring_categories)
from stats.models import AidViewEvent, AidSearchEvent, Event


@app.task
def log_aidviewevent(aid_id, querystring='', source=''):
    source_cleaned = get_subdomain_from_host(source)
    querystring_cleaned = clean_search_querystring(querystring)

    AidViewEvent.objects.create(
            aid_id=aid_id,
            querystring=querystring_cleaned,
            source=source_cleaned)


@app.task
def log_aidsearchevent(querystring='', source='', results_count=0):
    """
    Method to cleanup/populate the AidSearchEvents
    Run asynchronously to avoid slowing down requests.
    """
    source_cleaned = get_subdomain_from_host(source)
    querystring_cleaned = clean_search_querystring(querystring)

    # sometimes we query our API for internal (e.g. admin) purposes
    # we don't want to log these searches
    is_internal_search = get_querystring_value_list_from_key(querystring_cleaned, 'internal')  # noqa

    if not is_internal_search:  # noqa
        targeted_audiences = get_querystring_value_list_from_key(querystring, 'targeted_audiences') or None  # noqa
        perimeter = get_querystring_perimeter(querystring)
        text = get_querystring_value_from_key(querystring, 'text')
        text_cleaned = text[:256] if text else ''

        event = AidSearchEvent.objects.create(
            querystring=querystring_cleaned,
            source=source_cleaned,
            results_count=results_count,
            targeted_audiences=targeted_audiences,
            perimeter=perimeter,
            text=text_cleaned)

        themes = get_querystring_themes(querystring)
        categories = get_querystring_categories(querystring)
        event.themes.set(themes)
        event.categories.set(categories)


def log_event(category, event, meta='', source='', value=None):
    Event.objects.create(
        category=category,
        event=event,
        meta=meta,
        source=source,
        value=value)
