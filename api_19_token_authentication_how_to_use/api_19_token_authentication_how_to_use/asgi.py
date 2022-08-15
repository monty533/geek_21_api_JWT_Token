"""
ASGI config for api_19_token_authentication_how_to_use project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_19_token_authentication_how_to_use.settings')

application = get_asgi_application()
