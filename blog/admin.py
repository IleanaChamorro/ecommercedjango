from django.contrib import admin
from .models import Categoria, Noticias
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class NoticiasAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticias, NoticiasAdmin)