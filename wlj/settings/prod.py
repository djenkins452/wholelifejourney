from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "wholelifejourney.com",
    "www.wholelifejourney.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://wholelifejourney.com",
    "https://www.wholelifejourney.com",
]

MIDDLEWARE.insert(
    1, "whitenoise.middleware.WhiteNoiseMiddleware"
)

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
