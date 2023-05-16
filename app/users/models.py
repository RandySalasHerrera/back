from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    fecha = models.DateField(verbose_name="Fecha de nacimiento", blank=True, null=True)
    # Agrega más campos según tus necesidades
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
