from django.contrib import admin
from .models import Project

# Register your models here.
# Extender las funcionalidades del panel admin
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Se le agrega al administrador el tema de "Projects" pero además, se extiende la funcionalidad del panel de admin
# y a los projects se les agrega esos dos campos "readonly"
admin.site.register(Project, ProjectAdmin)