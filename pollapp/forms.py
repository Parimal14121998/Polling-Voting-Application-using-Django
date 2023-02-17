from django import forms
from .models import pollmodel

class pollform(forms.ModelForm):
	class Meta:
		model=pollmodel
		fields=["qts","op1","op2","op3"]
		widgets={"qts":forms.Textarea(attrs={"rows":4,"cols":30,"placeholder": "Enter your question"})}

