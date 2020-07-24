from channels.db import database_sync_to_async

from accounts.models import User
from comments.models import Comment
from post.models import Post


@database_sync_to_async
def update_comment(comment_id, **data):
    data_to_update = {
        'commenter': User.objects.get(pk=data['commenter_id']),
        'post': Post.objects.get(pk=data['post_id']),
        'reply_to': Comment.objects.get(pk=data['reply_to_id']),
        'content': data['content']
    }
    Comment.objects.filter(pk=comment_id).update(**data_to_update)
    return Comment.objects.get(pk=comment_id)