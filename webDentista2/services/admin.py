from django.contrib import admin
from .models import Service, Category

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías "

admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
