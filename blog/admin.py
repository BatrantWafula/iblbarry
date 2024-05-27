# admin.py
from django.contrib import admin
from .models import Post, Subscriber

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Ensure 'created_at' is used correctly
    search_fields = ('title', 'content')

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')  # Ensure 'created_at' is used correctly
    list_filter = ('created_at',)  # Filter by 'created_at'
    search_fields = ('email',)

admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
