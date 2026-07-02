from django import forms

class TituloForm(forms.Form):
    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Digite a descrição do título',
        
    )

class TituloUpdateForm(forms.Form):
    codigo = forms.IntegerField(
        required=True,
        help_text='Digite o código do título',
    )

    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Digite a nova descrição do título',
    )       

    