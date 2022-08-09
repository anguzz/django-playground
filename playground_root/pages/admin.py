from django.contrib import admin
from .models import Page #imports page model to admin view


# Register your models here.
admin.site.register(Page)

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering=('title',)
    search_field=('title',)

admin.site.register(Page, PageAdmin)

