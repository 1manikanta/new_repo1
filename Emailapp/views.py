from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmailForm  # Assuming you have a Django form for the email
from .models import SentEmail


def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_email = form.cleaned_data['recipient']

            try:
                # Send email using send_mail, not Email
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

                # Save information about sent email
                SentEmail.objects.create(
                    subject=subject,
                    message=message,
                    sender=settings.DEFAULT_FROM_EMAIL,
                    recipient=recipient_email
                )

                return HttpResponse('Email sent successfully!')
            except Exception as e:
                return HttpResponse(f'Error sending email: {e}')
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})
