from django import forms
from .models import Moo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MooForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={"placeholder":"Enter your Message", "class":"form-control",},), label="",)

    class Meta:
        model = Moo
        exclude = ("user","likes")

class SignupForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.widgets.Input(attrs={"placeholder":"Email:", "class":"form-input"}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self,*args,**kwargs):
        super(SignupForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-input'
        self.fields['username'].widget.attrs['placeholder'] = 'Username:'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password:'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Password again:'
        self.fields['password2'].label = ''