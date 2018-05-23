from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage, BadHeaderError
from django.template.loader import get_template
from .forms import ContactForm
from django.contrib import messages
from django.utils.safestring import mark_safe

def home(request):
    return render(request, 'oodlums/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            message = request.POST.get('message','')
            template = get_template('oodlums/contact_template.txt')
            context = ({
                    'name' : name,
                    'email' : email,
                    'message' : message,
                })
            content = template.render(context)
            fromEmail = email

            email = EmailMessage(
                "Oodlums contact form submission",
                content,
                'oodlum.rhymes@gmail.com',
                [email,],
                ['oodlum.rhymes@gmail.com'],
                )
            try:
                #email.send()
                messages.success(request, "We'll get back to you soon at '" + fromEmail + "'!")
            except BadHeaderError:
                messages.error(request, "Something went wrong, please try again")
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'oodlums/contact.html', {'form' : form})
