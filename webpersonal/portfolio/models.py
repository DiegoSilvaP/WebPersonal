from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    link = models.URLField(max_length=500, verbose_name="URL", blank=True, null=True)
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateField(auto_now_add=True, verbose_name="Creado") # Se autoañade la hora al crear esta instancia de proyecto
    updated = models.DateField(auto_now=True, verbose_name="Editado") # Se actualiza cuando se modifique

    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        # ordenamiento
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un -
        # para ordenar del mas nuevo al mas viejo
        ordering = ["-created"]

    def __str__(self):
        return self.title