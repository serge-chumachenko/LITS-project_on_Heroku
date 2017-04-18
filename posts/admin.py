from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'update']
    list_display_links = ['update']
    list_filter = ['update','timestamp']
    search_fields = ['title','content']
    list_editable = ['title']
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)