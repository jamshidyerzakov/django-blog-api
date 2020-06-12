from django.db import models
from taggit.managers import TaggableManager
from accounts.models import User


class Post(models.Model):
    """class Post for an article"""
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Author", related_name='authors')
    title = models.CharField(max_length=128, verbose_name="Title")
    short_content = models.TextField(max_length=1024)
    full_content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    date_updated = models.DateTimeField(auto_now=True)
    likes = models.IntegerField(verbose_name="likes")
    img = models.ImageField(verbose_name="Image")
    tags = TaggableManager(verbose_name="Tags", related_name="tags")
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name="Category",
        related_name='posts'
    )

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


class Category(models.Model):
    """Categorizing posts"""
    category_title = models.CharField(max_length=128, verbose_name="Category title")
    description = models.TextField(verbose_name="Description", null=True)
    parent_category = models.ForeignKey('self',
                                        null=True,
                                        blank=True,
                                        on_delete=models.PROTECT,
                                        related_name="children",
                                        )

    class Meta:
        ordering = ('category_title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_title


class Comment(models.Model):
    """Comments for a post"""
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    reply_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.commenter.email)

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
