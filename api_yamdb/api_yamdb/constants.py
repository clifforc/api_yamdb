
USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'

ROLES = (
    (USER, 'User'),
    (MODERATOR, 'Moderator'),
    (ADMIN, 'Admin')
)

MAX_ROLE_LENGTH = max(len(role[0]) for role in ROLES)
USERNAME_MAX_LENGTH = 150
EMAIL_MAX_LENGTH = 254
CONFIRMATION_CODE_MAX_LENGTH = 150

NOT_ALLOWED_USERNAME = 'me'

