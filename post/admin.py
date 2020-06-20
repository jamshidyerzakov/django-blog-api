from django.contrib import admin
from .models import Post, Category
from django.contrib.auth.models import Permission


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Author', {'fields': ['author']}),
        ('Full content', {'fields': ['full_content']}),
        (None, {'fields': ['short_content']}),
        ('Likes', {'fields': ['likes']}),
        (None, {'fields': ['img']}),
        ('Tags', {'fields': ['tags']}),
        # ('Comments', {'fields': ['comments']}),
        ('Category', {'fields': ['category']}),
    ]
    list_display = ('author',
                    'title',
                    'short_content',
                    'full_content',
                    'likes',
                    'tags',
                    'category',
                    )
    list_filter = ['date_created']
    list_display_links = ('title', 'full_content')
    search_fields = ['title', 'category__name']
    save_on_top = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title', 'description')
    search_fields = ['category_title']

admin.site.register(Permission)
admin.site.site_title = "Django Blog"
admin.site.site_header = "Django Blog"
