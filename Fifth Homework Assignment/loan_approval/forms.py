from django import forms
from .models import LoanApproval

class LoanForm(forms.ModelForm):
	class Meta:
		model=LoanApproval
		fields='__all__'