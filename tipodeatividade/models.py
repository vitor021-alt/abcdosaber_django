from django.db import models

# Create your models here.
class Tipodeatividade(models.Model):
    codigo = models.AutoField(
        primary_key=True,
        help_text="Código de tipo de atividade",
    )

    descricao= models.CharField(
        max_length=70,
        null=False,
        help_text="Informe a descrição de tipo de atividade",
    )

    def __str__(self):
        return f'{self.codigo} {self.descricao}'
        