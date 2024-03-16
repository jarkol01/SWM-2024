from .base import *

SECRET_KEY = "secret_key"

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "SWM2024"),
        "USER": env("POSTGRES_USER", "SWM2024"),
        "PASSWORD": env("POSTGRES_PASSWORD", "SWM2024"),
        "HOST": env("POSTGRES_HOST", "localhost"),
    }
}

ALLOWED_HOSTS = ["*"]
