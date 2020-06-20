from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework import serializers
from .models import Post
from rest_framework.pagination import PageNumberPagination
#


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PostFilter(filters.FilterSet):
    tags = CharFilterInFilter(field_name='tags__name', lookup_expr='in', distinct=True)

    class Meta:
        model = Post
        fields = ['category', 'tags']


class PaginationPosts(PageNumberPagination):
    page_size = 10
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'count': self.page.paginator.count,
            'results': data
        })


class RecursiveSerializer(serializers.Serializer):
    """Recursive display of children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
