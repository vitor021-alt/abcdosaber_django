from django.db import models

# Create your models here.
class Aluno(models.Model):
    matricula = models.AutoField(
        primary_key=True,
        help_text="Matrícula do aluno",
    )

    nome = models.CharField(
        max_length=100,
        null=False,
        help_text="Nome do aluno",
    )

    datainicial= models.DateField(
        max_length=70,
        null=False,
        help_text="Informe a data inicial do aluno",
    )

    datafinal= models.DateField(
        max_length=70,
        null=True,
        blank=True,
        help_text="Informe a data final do aluno",
    )

    def __str__(self):
        return f'{self.matricula} {self.nome} {self.datainicial} {self.datafinal}'