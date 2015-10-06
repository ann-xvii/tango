from django.contrib import admin
from rango.models import Category, Page, UserProfile


class PagesInline(admin.TabularInline):
    model = Page


# @admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

    list_display = ("name", )

    inlines = [
        PagesInline
    ]


class PageAdmin(admin.ModelAdmin):
    list_display = ("category", "title", "url")
    model = Page


admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
