from django.db import models

# Create your models here.
class Persona(models.Model):
    id_persona = models.CharField(primary_key=True, max_length=20, verbose_name='Rut')
    name = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellido')
    email = models.EmailField(max_length=254, verbose_name='Correo')
    image = models.URLField(max_length=254, verbose_name='Link Imagen')

    class Meta:
        verbose_name = 'persona'
        verbose_name_plural = 'personas'
        ordering = ['lastname', 'name', 'id_persona']
    
    def __str__(self):
        return self.lastname + ' ' +  self.name + " (" + self.id_persona + ")"
