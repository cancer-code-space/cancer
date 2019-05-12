from .base_test import *

# site is gaborone
SITE_ID = 10

WSGI_APPLICATION = 'cancer.wsgi.gaborone-uat.application'


ALLOWED_HOSTS = [
    'localhost', '127.0.0.1',
    'gaborone.uat.cancer.bhp.org.bw']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': os.path.join(MYSQL_DIR, 'uat.conf'),
        },
    },
}

TIME_ZONE = 'Africa/Gaborone'
