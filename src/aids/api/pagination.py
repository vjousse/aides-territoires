from rest_framework.pagination import PageNumberPagination


class AidsPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'size'
    max_page_size = 200
