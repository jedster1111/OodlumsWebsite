from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oodlums$Data',
        'USER': 'oodlums',
        'PASSWORD': 'Myjasmine10',
        'HOST': 'oodlums.mysql.pythonanywhere-services.com',
        }
    }


ALLOWED_HOSTS = [
    'jedster1111.pythonanywhere.com',
    'www.oodlums.com',
    'oodlums.com',
    'www.oodlums.co.uk',
    'oodlums.co.uk',
]