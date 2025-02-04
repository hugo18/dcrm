from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Endereço de email'}))
    first_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nome'}))
    last_name =  forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Sobrenome'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text =  '<span class="form-text text-muted"><small>No máximo 150 caracteres. Somente letras, dígitos e @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sua senha não pode ser muito similar com suas outras informações.</li><li>Sua senha precisa ter no mínimo 8 caracteres</li><li>Sua senha não pode ser uma senha comumente usada.</li><li>Sua senha não pode ser inteiramente numérica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text =  '<span class="form-text text-muted"><small>Digite novamente sua senha, para verificação.</small></span>'
