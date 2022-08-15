"""
ASGI config for api_16_authentication_permission_func_based_view project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_16_authentication_permission_func_based_view.settings')

application = get_asgi_application()
