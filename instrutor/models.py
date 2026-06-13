from django.db import models

from titulo.models import Titulo

# Create your models here.
class Instrutor(models.Model):
    id = models.AutoField(
        primary_key=True,
        help_text="ID do instrutor",
    )

    rg= models.CharField(
        max_length=11,
        null=False,
        help_text="informe o RG do instrutor",
    )

    nome= models.CharField(
        max_length=70,
        null=False,
        help_text="Informe o nome do instrutor",
    )

    dataNascimento= models.DateField(
        max_length=10,
        null=True,
        help_text="Informe a data de nascimento",
    )


    telefone= models.CharField(
        max_length=9,
        null=True,
        help_text="Informe o telefone do instrutor",
    
    )

    ddd= models.CharField(
        max_length=3,
        null=True,
        help_text="Informe o DDD do instrutor",
    )

    codigo_titulo= models.ForeignKey(
        Titulo,
        null=True,
        blank=True,
        related_name='instrutores',
        on_delete=models.SET_NULL,
        db_column='codigo_titulo',
        help_text="Informe o código do título do instrutor",
    )



    


    def __str__(self):
        return f'{self.id} {self.rg} {self.nome} {self.dataNascimento} {self.telefone} {self.ddd} {self.codigo_titulo}'