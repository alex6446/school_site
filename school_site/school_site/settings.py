"""
Django settings for school_site project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')2%l9n1mr$8&=ji^4(--6s7_yvg+221=v(z1r*w-c%+)bvae8m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '15f20de6.ngrok.io',
    'localhost'
]

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    # 'easy_maps',
    'crispy_forms',
    'django.contrib.sites',
    'fluent_contents.plugins.googledocsviewer',
    'fluent_contents',
    'django_wysiwyg',
    'filebrowser',
    'tinymce',
    'core.apps.CoreConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'school_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'school_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ru-ua'

TIME_ZONE = 'Etc/GMT-3'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'core/static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static/js/tinymce/tinymce.min.js")
#TINYMCE_JS_URL = os.path.join(MEDIA_URL, "js/tinymce/tinymce.min.js")
#TINYMCE_COMPRESSOR = True

TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 920,
    'language': 'ru',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor colorpicker save link image media preview codesample 
            table code lists fullscreen  insertdatetime  nonbreaking
             directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak paste
            ''',
    'toolbar1': '''
            bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | link image media | 
            codesample | visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor | preview code fullscreen |
            ''',
    'toolbar2': '''
            alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            ''',
    'menubar': True,
    'statusbar': True,
    'visual': True,
    'fontsize_formats': "8pt 10pt 12pt 14pt 16pt 18pt 20pt 22pt 24pt 28pt 32pt 36pt 42pt 48pt",
    'forced_p_newlines': False,
    'forced_br_newlines': True,
    'forced_root_block': '',
    }

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.net'
EMAIL_HOST_USER = 'school2testing321@gmail.com'
EMAIL_HOST_PASSWORD = 'testing321'
EMAIL_PORT = 587
# ACCOUNT_EMAIL_SUBJECT_PREFIX = 'school2'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# EASY_MAPS_GOOGLE_KEY = 'AIzaSyCwRFDROO70Wg4OJe9XmzSbM6pht-jOzBk'

#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025

"""STATICFILES_DIRS= [
    os.path.join(BASE_DIR , "static")
]"""
#DEFAULT_PATH_TINYMCE = os.path.join(BASE_DIR, "static/js/tinymce/")
#FILEBROWSER_DIRECTORY = os.path.join(BASE_DIR, 'media')


