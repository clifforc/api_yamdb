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

    subject = 'YaMDb Registration Confirmation'
    message = f'Your confirmation code is: {confirmation_code}'
    from_email = 'noreply@yamdb.com'
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)
