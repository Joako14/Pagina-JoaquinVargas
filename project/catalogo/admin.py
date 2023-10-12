from django.contrib import admin

from . import models

admin.site.site_title = "Catalogo"
admin.site.site_header = "Catalogo Cyclon"


@admin.register(models.MarcaCategoria)
class MarcaCategoriaAdmin(admin.ModelAdmin):
    """
    - list_display: tupla que especifica los campos que se mostrarán en la lista de objetos
    - search_fields: tupla que especifica los campos por los que se puede buscar en la lista de objetos
    - list_filter: tupla que especifica los campos por los que se puede filtrar en la lista de objetos
    - ordering: tupla que especifica el orden en que se mostrarán los objetos
    """

    list_display = ("marca",)
    search_fields = ("marca",)
    list_filter = ("marca",)
    ordering = ("marca",)
    
@admin.register(models.ModeloCategoria)
class ModeloCategoriaAdmin(admin.ModelAdmin):

    list_display = ("modelo",)
    search_fields = ("modelo",)
    list_filter = ("modelo",)
    ordering = ('id',)
    
@admin.register(models.AñoCategoria)
class AñoCategoriaAdmin(admin.ModelAdmin):

    list_display = ("año",)
    search_fields = ("año",)
    list_filter = ("año",)
    ordering = ('id',)
    
@admin.register(models.BateriaCategoria)
class BateriaCategoriaAdmin(admin.ModelAdmin):

    list_display = ("bateria",)
    search_fields = ("bateria",)
    list_filter = ("bateria",)
    ordering = ('bateria',)

@admin.register(models.Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    list_display = (
        "marca",
        "modelo",
        "año",
        "bateria",
        "descripcion",
        "fecha_actualizacion",
    )
    list_display_links = ("marca", "modelo", "año",)
    search_fields = ("marca", "modelo", "año",)
    ordering = (
        "marca", "modelo", "año",
    )
    list_filter = ("marca", "modelo", "año",)
    date_hierarchy = "fecha_actualizacion"
