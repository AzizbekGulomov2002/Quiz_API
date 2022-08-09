
from distutils import core
from pathlib import Path
import os
from core.jazzmin import JAZZMIN_SETTINGS

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# DJANGO_SETTINGS_MODULE=core.settings

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d-8azxo3*zu163hdnn#@-n(io73!&+jkwvhxpze18)+tlo-=2#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1","quizapp2002.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quiz',
    'ckeditor',
    'rest_framework',
    
]
CKEDITOR_CONFIGS = {
    'savol_awesome_ckeditor': {
        'height': 250,
        'width': '100%',
    },
    'awesome_ckeditor': {
        'height': 100,
        'width': '100%',
    },
}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI_APPLICATION = 'quiz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'uz-uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
import os
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'root')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from .jazzmin import JAZZMIN_SETTINGS
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS 

# JAZZMIN_SETTINGS["show_ui_builder"] = True
# JAZZMIN_UI_TWEAKS = {
#     "navbar_small_text": False,
#     "footer_small_text": False,
#     "body_small_text": False,
#     "brand_small_text": False,
#     "brand_colour": "navbar-success",
#     "accent": "accent-teal",
#     "navbar": "navbar-dark",
#     "no_navbar_border": False,
#     "navbar_fixed": False,
#     "layout_boxed": False,
#     "footer_fixed": False,
#     "sidebar_fixed": False,
#     "sidebar": "sidebar-dark-info",
#     "sidebar_nav_small_text": False,
#     "sidebar_disable_expand": False,
#     "sidebar_nav_child_indent": False,
#     "sidebar_nav_compact_style": False,
#     "sidebar_nav_legacy_style": False,
#     "sidebar_nav_flat_style": False,
#     "theme": "cyborg",
#     "dark_mode_theme": None,
#     "button_classes": {
#         "primary": "btn-primary",
#         "secondary": "btn-secondary",
#         "info": "btn-info",
#         "warning": "btn-warning",
#         "danger": "btn-danger",
#         "success": "btn-success",
#     },
# }