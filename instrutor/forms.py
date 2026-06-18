from django import forms

class InstrutorForm(forms.Form):
    nome= forms.CharField(
        max_length=70,
        required=True,
        help_text="Informe o nome do instrutor",
    )

    rg= forms.CharField(
        max_length=11,
        required=True,
        help_text="informe o RG do instrutor",
    )

    dataNascimento= forms.DateField(
        required=False,
        help_text="Informe a data de nascimento",
    )

    ddd= forms.CharField(
        max_length=3,
        required=False,
        help_text="Informe o DDD do instrutor",
    )

    telefone= forms.CharField(
        max_length=9,
        required=False,
        help_text="Informe o telefone do instrutor",
    
    )
