from .base import *

DEBUG = True

STATICFILES_DIRS = [
    BASE_DIR / "wlj" / "static",
]

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
