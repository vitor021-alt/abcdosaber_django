from django import forms

class InstrutorForm(forms.Form):
    rg = forms.CharField(
        max_length=15,
        required=False,
        help_text="Informe o RG do instrutor"
    )
    
    nome = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe o nome do Instrutor'
    )

    dataNascimento = forms.DateField(
        required=True,
        help_text="Informe a data de nascimento do instrutor"
    )
     
    ddd = forms.CharField(
        max_length=3,
        required=False,
        help_text='Informe o DDD do instrutor'
    )    

    telefone = forms.CharField(
        max_length=9,
        required=False,
        help_text='Informe o telefone do instrutor'
    )    
    
    codigo_titulo = forms.IntegerField(
        required=False,
        help_text='Informe o código do título do instrutor'
    )    
    

class InstrutorUpdateForm(forms.Form):
    id = forms.IntegerField(
        required=True,
        widget=forms.HiddenInput()
    )
     
    nome = forms.CharField(
        max_length=70,
        required=True,
        help_text='Informe o nome do Instrutor'
    )

    rg = forms.CharField(
        max_length=15,
        required=False,
        help_text="Informe o RG do instrutor"
    )

    dataNascimento = forms.DateField(
        required=True,
        help_text="Informe a data de nascimento do instrutor"
    ) 

    ddd = forms.CharField(
        max_length=3,
        required=False,
        help_text='Informe o DDD do instrutor'
    )    

    telefone = forms.CharField(
        max_length=9,
        required=False,
        help_text='Informe o telefone do instrutor'
    )    
    
    codigo_titulo = forms.IntegerField(
        required=False,
        help_text='Informe o código do título do instrutor'
    )

