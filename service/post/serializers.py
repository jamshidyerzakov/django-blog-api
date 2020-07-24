from abc import ABC
from typing import List

from rest_framework import serializers
from rest_framework.exceptions import ParseError


class FilterCategorySerializer(serializers.ListSerializer):
    """Filtering categories, only parents"""

    def to_representation(self, categories):
        if isinstance(categories, list):
            return super().to_representation([category for category in categories if not category.children_categories])
        return super().to_representation(categories.filter(children_categories=None))


class TagListSerializer(serializers.ListField):

    def from_native(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_native(self, obj):
        return obj.all()

    def to_representation(self, data):
        """
        List of object instances -> List of dicts of primitive datatypes.
        """

        if isinstance(data, list):
            return [self.child.to_representation(item) if item is not None else None for item in data]
        return [self.child.to_representation(item.name) if item is not None else None for item in data.all()]
