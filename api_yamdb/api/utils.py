from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from api_yamdb import settings


def send_confirmation_code(user):
    """
    Function that sends confirmation code to the recipient.
    """
    confirmation_code = default_token_generator.make_token(user)
    send_mail('YaMDb Registration Confirmation',
              f'Your confirmation code is: {confirmation_code}',
              settings.REGISTRATION_FROM_EMAIL,
              [user.email])
