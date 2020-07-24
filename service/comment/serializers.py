from typing import List

from rest_framework import serializers


class FilterCommentSerializer(serializers.ListSerializer):
    """Filtering comments, only parents"""
    def to_representation(self, comments):
        if isinstance(comments, list):
            return super().to_representation([comment for comment in comments if not comment.reply_to])
        return super().to_representation(comments.filter(reply_to=None))
