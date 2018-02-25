from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your email'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}))

    #test