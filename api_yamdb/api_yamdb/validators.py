from datetime import date

from django.core.exceptions import ValidationError

from api_yamdb import constants


def validate_username_not_me(value):
    if value == constants.NOT_ALLOWED_USERNAME:
        raise ValidationError(
            {"username": f"Использовать имя '{value}' "
                         "в качестве username запрещено."}
        )


def validate_max_year(value):
    if value <= date.today().year:
        return value
    else:
        raise ValidationError('Введите год произведения, не больше текущего.')
