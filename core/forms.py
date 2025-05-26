from django import forms

class QuoteRequestForm(forms.Form):
    name = forms.CharField(max_length=100, label="Full Name", widget=forms.TextInput(attrs={'placeholder': 'Your full name'}))
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    phone = forms.CharField(max_length=20, required=False, label="Phone Number", widget=forms.TextInput(attrs={'placeholder': 'Optional phone number'}))
    company = forms.CharField(max_length=100, required=False, label="Company Name", widget=forms.TextInput(attrs={'placeholder': 'Your company (optional)'}))
    service = forms.CharField(widget=forms.HiddenInput())  # hidden field for the service name
    message = forms.CharField(label="Additional Details", required=False, widget=forms.Textarea(attrs={'placeholder': 'Tell us more about your requirements...', 'rows': 4}))

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name", widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(label="Your Email", widget=forms.EmailInput(attrs={'placeholder': 'Your email'}))
    subject = forms.CharField(max_length=150, label="Subject", widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'placeholder': 'Your message...', 'rows': 5}))
