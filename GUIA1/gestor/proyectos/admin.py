from django.contrib import admin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "fecha_inicio", "activo")
    search_fields = ("nombre",)
    list_filter = ("activo",)

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "proyecto", "hecho")
    list_filter = ("hecho", "proyecto")
    search_fields = ("titulo",)

