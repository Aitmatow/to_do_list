from django.contrib import admin
from webapp.models import Tasks


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'description', 'status', 'done_date', 'detailed_description']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'done_date', 'detailed_description']
    readonly_fields = ['done_date']
    list_display_links = ['pk']

# Register your models here.
admin.site.register(Tasks, ArticleAdmin)