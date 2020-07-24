from django_filters import rest_framework as filters
from post.models import Post


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilter(filters.FilterSet):
    """Filtering posts by tag and category name"""
    tags = CharFilterInFilter(field_name='tags__name', lookup_expr='in', distinct=True)

    class Meta:
        model = Post
        fields = ['category', 'tags']