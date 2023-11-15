"""
WSGI config for crashblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR / "crashblog"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crashblog.settings')

application = get_wsgi_application()
