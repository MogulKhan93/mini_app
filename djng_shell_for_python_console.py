"""
Just copy this code and paste it into the Python Console
"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_app.settings")
# replace "my_app" with the name of your project

import django
django.setup()

from django.core.management import call_command
