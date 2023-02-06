from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    # Agrega más campos según tus necesidades
    
    class Meta:
        db_table = "usuario" # nombre de la tabla en la base de datos