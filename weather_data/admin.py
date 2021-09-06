from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin.actions import delete_selected as delete_selected_


# ovverride delete in admin
def delete_selected(modeladmin, request, queryset):
    if request.POST.get('post'):
        for obj in queryset:
            related_weather_data=Weather_Data.objects.filter(
                                       date_time__gte=obj.start_date
                                       ).filter(
                                       date_time__lte=obj.end_date
                                       )
            [data.delete() for data in related_weather_data]
            obj.delete()
    else:
        return delete_selected_(modeladmin, request, queryset)
delete_selected.short_description = "Delete selected objects"


class MyModelAdmin(admin.ModelAdmin):
    actions = [delete_selected]


admin.site.register(Weather_Data)
admin.site.register(Summary_Data,MyModelAdmin)
