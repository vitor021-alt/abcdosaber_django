from django import forms


class TurmaForm(forms.Form):
    horarioAula= forms.TimeField(
        required=True,
        help_text="informe o horario da aula",
    )

    duracaoAula= forms.TimeField(
        required=True,
        help_text="Informe a duração da aula",
    )

    dataInicial= forms.DateField(
        required=True,
        help_text="Informe a data inicial",
    )

    codigoTipoAtividade= forms.CharField(
        max_length=70,
        required=True,
        help_text="Informe o código do tipo de atividade",
    )

    matriculaMonitor= forms.CharField(
        max_length=70,
        required=True,
        help_text="Informe o registro do monitor",
    )

    idInstrutor= forms.CharField(
        required=True,
        help_text="Informe o ID do instrutor",
    )