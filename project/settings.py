import os
from dotenv import load_dotenv
from environs import Env

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

env_path = os.path.join(basedir, 'env', '.env')
load_dotenv(dotenv_path=env_path)

env = Env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.getenv('BD_HOST'),
        'PORT': os.getenv('BD_PORT'),
        'NAME': os.getenv('BD_NAME'),
        'USER': os.getenv('BD_USER'),
        'PASSWORD': os.getenv('BD_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEBUG = env.bool("DEBUG")
