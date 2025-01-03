from django.contrib import admin
from .models import Menu, ItemReview, Store, ItemCertificate

# Register your models here.

class ItemreviewInLine(admin.TabularInline):
    model = ItemReview
    extra = 2

class ItemVarietyAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
    inlines = [ItemreviewInLine]

class StoresAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("item_varieties",)

class ItemCertificateAdmin(admin.ModelAdmin):
    list_display = ("item", "certificate")

admin.site.register(Menu, ItemVarietyAdmin)
admin.site.register(Store, StoresAdmin)
admin.site.register(ItemCertificate, ItemCertificateAdmin)
