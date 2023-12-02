from rest_framework . pagination import LimitOffsetPagination




class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'my_limit'
    offset_query_param = 'myoffset'
    max_limit = 3
