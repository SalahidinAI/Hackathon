from rest_framework.pagination import PageNumberPagination

class OneObjectPagination(PageNumberPagination):
    page_size = 1