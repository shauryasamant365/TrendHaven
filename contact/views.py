from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def contact(request):
    post = request.POST
    if request.method == 'POST':
        name = post['name']
        email = post['email']
        subject = post['subject']
        message = post['message']
        Contact.objects.create(name=name, email=email,
                               subject=subject, message=message).save()

        # Send a mail to notify me
        subject = f"Contact recieved from {name} - TrendHaven"
        body = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            Message: {message}

            Thank you Sir Shaurya, 
            for reading this email from your 
            busy schedule (●'◡'●);
        """
        from_email = "shauryasamant365@gmail.com"
        to_emails = ["shauryasamant365@gmail.com"]

        send_mail(subject, body, from_email, to_emails)

        messages.success(
            request, 'Your message was sent successfully. We\' get back to you via your email provided.')
        return redirect('index')
    else:
        return render(request, 'contact/contact.html')
