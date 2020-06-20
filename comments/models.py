from django.db import models


class Comment(models.Model):
    """Comments for a post"""
    commenter = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name="commenter")
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.commenter.email)

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
