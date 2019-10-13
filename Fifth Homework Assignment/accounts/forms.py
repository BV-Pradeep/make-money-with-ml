from django import forms


class RegisterForm(forms.Form):
	first_name=forms.CharField(max_length=20,required=True)
	last_name=forms.CharField(max_length=20,required=False)
	username=forms.CharField(max_length=20,required=True)
	email=forms.EmailField(required=True)
	password= forms.CharField(widget=forms.PasswordInput,required=True)
	confirm_password= forms.CharField(widget=forms.PasswordInput,required=True)

	
class LoginForm(forms.Form):
	username=forms.CharField(max_length=20,required=True)
	password= forms.CharField(widget=forms.PasswordInput,required=True)
	