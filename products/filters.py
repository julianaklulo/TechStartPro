from django_filters import rest_framework as filters


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="contains")


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="contains")
    description = filters.CharFilter(lookup_expr="contains")
    price = filters.NumberFilter(lookup_expr="exact")
    categories__name = filters.CharFilter(lookup_expr="contains")
