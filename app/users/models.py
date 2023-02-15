from django.db import models

class User(models.Model):
    pk_tjornada = models.IntegerField(),
    codigo = models.CharField(max_length=100),
    author_rc = models.CharField(max_length=100),
    clients_rc = models.CharField(max_length=100)
    # Agrega más campos según tus necesidades
    
    class Meta:
        # db_table = "TJORNADA" # nombre de la tabla en la base de datos
        db_table = "ACADEMICO_TESTV0.TJORNADA"
        managed = False
        # db_schema = 'ACADEMICO_TESTV0'