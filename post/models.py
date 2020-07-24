from django.db import models
from taggit.managers import TaggableManager
from .managers import PostManager


class Post(models.Model):
    """Model Post for an article"""
    author = models.ForeignKey(
        'accounts.Author',
        on_delete=models.PROTECT,
        verbose_name="Author",
        related_name='authors'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name="Category",
        related_name='posts'
    )

    title = models.CharField(max_length=128, verbose_name="Title")
    img = models.ImageField(verbose_name="Image for a post")
    content = models.TextField(verbose_name="Content")

    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    tags = TaggableManager(verbose_name="Tags", related_name="tags", blank=True)
    likes = models.IntegerField(verbose_name="Likes", default=0)
    views = models.IntegerField(verbose_name="Views", default=0)

    objects = PostManager()

    class Meta:
        ordering = ('-date_created',)
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title[:50]


class Category(models.Model):
    """Categorizing posts"""
    title = models.CharField(max_length=128, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    img = models.ImageField(verbose_name="Image for a category")
    children_categories = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        verbose_name="Parent category",
        related_name="children",
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title[:50]
