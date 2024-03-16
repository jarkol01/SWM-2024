from django.contrib import admin

from SWM2024.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'issuer', 'start_timestamp', 'end_timestamp', 'location', 'price', 'visible')
    list_filter = ('issuer', 'start_timestamp', 'end_timestamp', 'location', 'price', 'visible')
    search_fields = ('title', 'short_description', 'issuer', 'start_timestamp', 'end_timestamp', 'location', 'price', 'visible')
