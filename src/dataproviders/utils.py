import csv
from html import unescape
from unicodedata import normalize
from urllib.parse import urljoin

from bs4 import BeautifulSoup as bs

from categories.models import Theme, Category


REMOVABLE_TAGS = ['script', 'style']
ALLOWED_TAGS = [
    'p', 'ul', 'ol', 'li', 'strong', 'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'br', 'a', 'iframe',
]
ALLOWED_ATTRS = ['href', 'src', 'alt', 'width', 'height', 'style',
                 'allow', 'frameborder', 'allowfullscreen',  # to display iframe
                 'target', 'rel']  # for links opening in a new tab


def content_prettify(raw_text, more_allowed_tags=[], more_allowed_attrs=[], base_url=None):
    """Clean imported data.

    We import data from many data sources, and it's not always directly
    usable to say the least. This method performs a list of several
    content beautification so we can safely include ugly data on our site:

     * removes escaped html characters
     * converts weird quote chars and use standard chars instead
     * normalize unicode characters
     * removes all `script` html tags
     * removes most of html tags (but leave their content)
     * removes all html tag attributes
     * replaces relative urls with absolute ones
     * autoindent existing html
    """
    allowed_tags = ALLOWED_TAGS + more_allowed_tags
    allowed_attrs = ALLOWED_ATTRS + more_allowed_attrs

    unescaped = unescape(raw_text or '')
    unquoted = unescaped \
        .replace('“', '"') \
        .replace('”', '"') \
        .replace('’', "'") \
        .replace('target="_blank"', 'target="_blank" rel="noopener"')
    normalized = normalize('NFKC', unquoted)

    # Cleaning html markup
    soup = bs(normalized, features='html.parser')
    tags = soup.find_all()
    for tag in tags:
        # Some tags must be removed altogether
        # We remove the tag and all it's content.
        # We alse clear empty tags.
        if tag.name in REMOVABLE_TAGS or not tag.name:
            tag.decompose()

        # Remaining tags must be cleaned
        else:
            if tag.name in allowed_tags:
                attrs = list(tag.attrs.keys())
                for attr in attrs:
                    if attr not in allowed_attrs:
                        tag.attrs.pop(attr)

                # Remove tags with no content
                if not tag.contents and tag.name not in ['br', 'img', 'iframe']:
                    tag.decompose()

                # Remove tags with empty strings (or newlines, etc.)
                elif tag.string and not tag.string.strip() and tag.name not in ['iframe']:
                    tag.decompose()

                # Replace relative urls with absolute ones
                if tag.name == 'a' and base_url:
                    tag['href'] = urljoin(base_url, tag['href'])

            # Some tags are not allowed, but we do not want to remove
            # their content.
            else:
                tag.unwrap()

    prettified = soup.prettify()

    return prettified


def mapping_categories(categories_mapping_csv_path, source_column_name, at_column_names):
    """
    Method to extract categories mapping from a specified csv file
    """
    categories_dict = {}

    with open(categories_mapping_csv_path) as csv_file:
        csvreader = csv.DictReader(csv_file, delimiter=",")
        for index, row in enumerate(csvreader):
            if row[at_column_names[0]]:
                categories_dict[row[source_column_name]] = []
                for column in at_column_names:
                    if row[column]:
                        category_list = get_category_list_from_name(row[column])
                        categories_dict[row[source_column_name]].extend(category_list)

    return categories_dict


def get_category_list_from_name(category_name):
    category_list = []

    try:
        category = Category.objects.get(name=category_name)
        category_list.append(category)
    except Category.DoesNotExist:
        # Maybe it's a Theme !
        # If it is, we'll need to add all of it's categories
        try:
            theme = Theme.objects.get(name=category_name)
            for category in theme.categories.all():
                category_list.append(category)
        except Theme.DoesNotExist:
            print(category_name)

    return category_list
