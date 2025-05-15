import os
import sys

sys.path.append('/var/www/script39_ru_usr/data/www/script39.ru') #путь до проекта django
sys.path.append('/home/u/user/fastuser/lib/python3.10/site-packages/') # путь до django
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings' #app - название проекта django.

import django
django.setup()

from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
