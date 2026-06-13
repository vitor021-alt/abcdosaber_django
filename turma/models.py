from django.db import models

from titulo.models import Titulo
from instrutor.models import Instrutor


# Create your models here.
class Turma(models.Model):
    numero = models.AutoField(
        primary_key=True,
        help_text="Numero da turma",
    )

    horarioAula= models.TimeField(
        max_length=100,
        null=False,
        help_text="informe o horario da aula",
    )

    duracaoAula= models.TimeField(
        max_length=70,
        null=False,
        help_text="Informe a duração da aula",
    )

    dataInicial= models.DateField(
        max_length=70,
        null=True,
        help_text="Informe a data inicial",
    )


    dataFinal= models.DateField(
        max_length=70,
        null=True,
        help_text="Informe a data final",
    )

    codigoTipoAtividade= models.CharField(
        max_length=70,
        null=True,
        help_text="Informe o código do tipo de atividade",
    )

    matriculaMonitor= models.CharField(
        max_length=70,
        null=True,
        help_text="Informe o registro do monitor",
    )

    idInstrutor= models.ForeignKey(
        Instrutor,
        null=True,
        blank=True,
        related_name='turmas',
        on_delete=models.SET_NULL,
        db_column='id_instrutor',
        help_text="Informe o ID do instrutor",
    )

    codigo_titulo= models.ForeignKey(
        Titulo,
        null=True,
        blank=True,
        related_name='turmas',
        on_delete=models.SET_NULL,
        db_column='codigo_titulo',
        help_text="Informe o código do título do instrutor",
    )






    def __str__(self):
        return f'{self.numero} {self.dataInicial} {self.dataFinal} {self.horarioAula} {self.duracaoAula} {self.codigo_titulo}'