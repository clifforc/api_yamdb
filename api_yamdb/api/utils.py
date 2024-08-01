import random
import string

from django.core.mail import send_mail


def generate_confirmation_code():
    """
    Function returns random code 8 digitsh length
    """
    return ''.join([random.choice(string.ascii_uppercase +
                                  string.ascii_lowercase +
                                  string.digits) for _ in range(8)])


def send_confirmation_code(user):
    """
    Function that sends confirmation code to the recipient
    """
    confirmation_code = generate_confirmation_code()
    user.confirmation_code = confirmation_code
    user.save()

    send_mail('YaMDb Registration Confirmation',
              f'Your confirmation code is: {confirmation_code}',
              'noreply@yamdb.com',
              [user.email])
