"""
WSGI config for myfirstapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

# This file is the entry point for WSGI-compatibel web servers to serve your project.
# WSGI(Web Server Gateway Interface) is a standard Python interface that allows web servers to communicate with web applications.
# When you deploy your Django project to a production server, this file's used by the web server to run your application.

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstapp.settings')

application = get_wsgi_application()
