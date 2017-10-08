from django.contrib import admin

from .models import News, Employment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'author', 'publish',
                    'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
admin.site.register(News, NewsAdmin)

admin.site.register(Employment)
