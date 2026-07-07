from django import forms

class AlunoForm(forms.Form):
    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Digite a descrição do aluno',
        
    )

class AlunoUpdateForm(forms.Form):
    codigo = forms.IntegerField(
        required=True,
        help_text='Digite o código do aluno',
    )

    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Digite a nova descrição do aluno',
    )       

    