from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=10, min_length=3)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
