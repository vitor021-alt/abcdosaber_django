from django import forms

class TipodeatividadeForm(forms.Form):
    descricao = forms.CharField(
        max_length=70,
        required=True,
        help_text='Digite a descrição do tipo de atividade',
        
    )

class TipodeatividadeUpdateForm(forms.Form):
    codigo = forms.IntegerField(widget=forms.HiddenInput())
    descricao = forms.CharField()
    