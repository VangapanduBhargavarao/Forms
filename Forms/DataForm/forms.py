from django import forms

class contact_form(forms.Form):
    name=forms.CharField(max_length=100,required=True,
                        widget=forms.TextInput(attrs={'placeholder':'abc'}))
    email=forms.EmailField(max_length=200,required=True,
                        widget=forms.EmailInput(attrs={'placeholder':'abc@gmail.com'}))
    feedback=forms.CharField(max_length=400,required=True,
                        widget=forms.TextInput(attrs={'placeholder':'give feedback'}))
