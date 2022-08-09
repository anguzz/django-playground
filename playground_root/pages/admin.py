from django.contrib import admin
from .models import Page #imports page model to admin 

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','update_date')
    ordering=('title',)
    search_field=('title',)

admin.site.register(Page, PageAdmin)

