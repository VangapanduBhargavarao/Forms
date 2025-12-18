from django import forms

class DataForm(forms.Form):
    name=forms.CharField(max_length=50,label="name",required=True,
                        widget=forms.TextInput(attrs={'placeholder':'Your_name'}))
    email=forms.EmailField(max_length=50,label="email",required=True,
                           widget=forms.EmailInput(attrs={'placeholder':"abc@gmail.com"}))
    message=forms.CharField(max_length=200,required=True,
                            widget=forms.Textarea(attrs={'placeholder':'give feedback'}))