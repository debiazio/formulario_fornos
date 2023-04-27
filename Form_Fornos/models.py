from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InsertedData(models.Model):
    NUM_PANELA = models.IntegerField(default=0, null=False, blank=False)
    FORNO_FUSAO = models.CharField(max_length=50, null=False, blank=False)
    HORA= models.DateTimeField(null=True)    
    USUARIO = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL, #--se for deletado altera pra NULL
        null=True,
        blank=False,
        related_name="user",
    )
    
    COMP_QUIMICA = models.CharField(max_length=50, null=True)
    TEMP_VAZ_ESPECIFICADO = models.CharField(max_length=50, null=False, blank=False)
    LIGA = models.IntegerField(null=True)
    REL_MAQUINAS = models.IntegerField(null=True)
    DENSIDADE_ESP = models.IntegerField(null=True)
    TEMPERATURA = models.IntegerField(null=True)
    FORNO_TORRE = models.CharField(max_length=50, null=True)
    N_P_TORRE = models.IntegerField(null=True)
    MKR = models.CharField(max_length=50, null=True)

    



