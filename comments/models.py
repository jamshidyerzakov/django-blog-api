from django.db import models


class Comment(models.Model):
    """Comments for a post"""
    commenter = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
        verbose_name="Author of the comment",
        related_name="commenter"
    )
    post = models.ForeignKey(
        'post.Post',
        on_delete=models.CASCADE,
        verbose_name="Related post for the comment",
        related_name='comments'
    )
    reply_to = models.ForeignKey(
        'self', null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Reply comment",
        related_name='children'
    )
    content = models.TextField(verbose_name="Content of the comment")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    def __str__(self):
        return 'Comment {} by {}'.format(self.content[:50], self.commenter.email)

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
