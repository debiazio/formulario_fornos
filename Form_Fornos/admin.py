from django.contrib import admin

from Form_Fornos.models import InsertedData

class ListandoApontamentos(admin.ModelAdmin):
    list_filter = ("USUARIO"),


admin.site.register(InsertedData, ListandoApontamentos)