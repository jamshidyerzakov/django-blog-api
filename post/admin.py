from django.contrib import admin

from .models import Post, Category

admin.site.site_title = "ProData"
admin.site.site_header = "ProData"

admin.site.register(Post)
admin.site.register(Category)

#
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     """Admin panel for Post model"""
#     fieldsets = [
#         ('Title', {'fields': ['title']}),
#         ('Author', {'fields': ['author']}),
#         ('Content', {'fields': ['content']}),
#         (None, {'fields': ['short_content']}),
#         ('Likes', {'fields': ['likes']}),
#         ('Views', {'fields': ['views']}),
#         (None, {'fields': ['img']}),
#         ('Tags', {'fields': ['tags']}),
#         ('Category', {'fields': ['category']}),
#     ]
#     list_display = ('author',
#                     'title',
#                     'content',
#                     'likes',
#                     'tags',
#                     'category',
#                     'views',
#                     )
#     list_filter = ['date_created']
#     list_display_links = ('author', 'title', 'content')
#     search_fields = ['title', 'category__name']
#     save_on_top = True
#
#
# @admin.register(Category)
# # class CategoryAdmin(admin.ModelAdmin):
# #     """Admin panel for Category model"""
# #     list_display = ('category_title', 'description')
# #     search_fields = ['category_title']

