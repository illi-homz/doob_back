from django.contrib import admin
from django.utils.html import format_html
from .models import Any, Banner, Event  # add this

admin.site.register(Any) # add this

def dublicate_ad(modeladmin, request, queryset):
    # клонирование выбранных Ad
    for el in queryset:
        el.pk = None
        el.save()


dublicate_ad.short_description = "Дублировать объект"

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'image_tag', 'is_main')
    list_editable = ['img', 'is_main']
    actions = [dublicate_ad]

    def image_tag(self, obj):
        return format_html('<img width="100" src="{}" />'.format(obj.img.url))

    image_tag.short_description = 'Картинка'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_editable = ['title']
    actions = [dublicate_ad]
