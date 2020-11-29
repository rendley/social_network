from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'id')
    search_fields = ('text',)
    list_filter = ('pub_date',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'id')
    search_fields = ('title',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)