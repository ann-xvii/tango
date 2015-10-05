from django.contrib import admin
from rango.models import Category, Page


class PagesInline(admin.TabularInline):
    model = Page


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ("name", )

    inlines = [
        PagesInline
    ]


class PageAdmin(admin.ModelAdmin):
    model = Page


admin.site.register(Page, PageAdmin)