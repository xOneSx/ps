from django.contrib import admin
from .models import Advertisement

# Register your models here.

class AdvAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'cr_date', 'auction', 'up_date', 'image']
    list_filter = ['auction', 'created_at',]
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image'),
            'classes': ['collapse']
        }),

        ('Финансы', {
            'fields': ('price', 'auction')
        })
    )

    @admin.action(description='Убрать возможость торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможость торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)



admin.site.register(Advertisement, AdvAdmin)