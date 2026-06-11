from django.db import models

from titulo.models import Titulo
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

    codigo_titulo= models.ForeignKey(
        Titulo,
        null=True,
        blank=True,
        related_name='titulos',
        on_delete=models.SET_NULL,
        db_column='codigo_titulo',
        help_text="Informe o código do título do instrutor",
    )




    def __str__(self):
        return f'{self.codigo} {self.descricao}'
        