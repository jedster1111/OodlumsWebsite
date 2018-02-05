from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.template import Context
from django.template.loader import get_template
from .forms import ContactForm

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

            email = EmailMessage(
                "Contact form submission",
                content,
                "Oodlums" + '',
                ['jedster1111@hotmail.co.uk'],
                headers = {'Reply-To' : email}
                )
            try:
                email.send();
            except BadHeaderError:
                return HttpResponse('Invalid Header Found')
            return redirect('contact')

    else:
        form = ContactForm()

    return render(request, 'oodlums/contact.html', {'form' : form})
