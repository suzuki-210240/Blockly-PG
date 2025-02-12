"""
WSGI config for Blockly project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blockly.settings')

application = get_wsgi_application()
application = whitenoise(application,root="/home/ec2-user/Blockly-PG/staticfiles")
