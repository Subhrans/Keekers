from django.contrib.auth import get_user_model
# from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
# from registration import View
class UserCreateForm(UserCreationForm):

    class Meta:
        fields=('username','email','password1','password2')
        model=get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='display name'
        self.fields['email'].label='display email'
class RegistrationView:
    pass
class checkoutForm(forms.Form):
    FirstName=forms.CharField(widget=forms.TextInput(attrs={
                                                            'class':'form-control',
                                                            'placeholder':"Enter your First Name",
                                                            'aria-label':'FirstName',
                                                            }))
    LastName=forms.CharField(widget=forms.TextInput(attrs={
                                                            'class':'form-control',
                                                            'aria-label':'LastName',
                                                            }))
    Email=forms.CharField(widget=forms.TextInput(attrs={
                                                        'class':'form-control',
                                                        'aria-label':'Email',
                                                        }))
    ContactNumber=forms.CharField(widget=forms.TextInput(attrs={
                                                                'class':'form-control',
                                                                'aria-label':'ContactNumber',
                                                                }))
    Address1=forms.CharField(widget=forms.TextInput(attrs={
                                                            'class':'form-control',
                                                            'aria-label':'Address1',
                                                            }))
    Address2=forms.CharField(widget=forms.TextInput(attrs={
                                                            'class':'form-control',
                                                            'aria-label':'Address2',
                                                            }))
