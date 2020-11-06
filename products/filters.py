from django_filters import rest_framework as filters


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="contains")

