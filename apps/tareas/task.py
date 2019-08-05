from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from test_celery import settings


@shared_task
def send_emails_users():
    asunto= 'mensaje de prubea'
    mensaje= 'Bienvenido, esto es un mensaje de prueba celery'
    users=User.objects.all()
    for x in users:
        send_mail(asunto,mensaje, settings.EMAIL_HOST_USER, [x.email], fail_silently=False)
     