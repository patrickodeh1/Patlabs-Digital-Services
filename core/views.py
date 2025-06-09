from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import QuoteRequestForm, ContactForm
from django.core.mail import send_mail
from django.conf import settings


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                subject=f"[Contact Form] {cd ['subject']}",
                message=(
                    f"Name: {cd['name']}\n"
                    f"Email: {cd['email']}\n\n"
                    f"Message:\n{cd['message']}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['patlabsdigitalservices@gmail.com'],
                fail_silently=False,
            )
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
            cd = form.cleaned_data
            send_mail(
                subject=f"[Quote Request] {cd['service']}",
                message=(
                    f"Name: {cd['name']}\n"
                    f"Email: {cd['email']}\n"
                    f"Phone: {cd.get('phone', 'N/A')}\n"
                    f"Company: {cd.get('company', 'N/A')}\n\n"
                    f"Message:\n{cd['message']}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['patlabsdigitalservices@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Thank you for your request! We'll get back to you shortly.")
            return redirect(reverse('get_quote'))
    else:
        initial_service = request.GET.get('service', '')
        form = QuoteRequestForm(initial={'service': initial_service})

    return render(request, 'quote_form.html', {'form': form})
