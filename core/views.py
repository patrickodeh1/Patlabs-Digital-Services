from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import QuoteRequestForm, ContactForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here, you can handle sending an email or saving to DB
            messages.success(request, "Thank you for reaching out! We will get back to you shortly.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



class ServicesPageView(TemplateView):
    template_name = 'services.html'

def get_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            # Here you could send email, save to DB, or process the data
            # For now, just display a success message and redirect
            messages.success(request, "Thank you for your request! We'll get back to you shortly.")
            return redirect(reverse('get_quote'))
    else:
        # If service is passed as GET param (e.g., ?service=Website Development)
        initial_service = request.GET.get('service', '')
        form = QuoteRequestForm(initial={'service': initial_service})

    return render(request, 'quote_form.html', {'form': form})