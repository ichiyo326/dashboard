"""
Django settings for config project.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-s4_c()p^t0_lrk7t710au_3-*po83rwynbuok5f_ae!db^lvk6'
DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # Django 標準アプリ
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # サードパーティ
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',

    # 自作アプリ
    'dashboard',
]

MIDDLEWARE = [
    # corsheaders は CommonMiddleware より前に置く
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',          # ← corsheaders の後
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation (省略)

# Internationalization (省略)

STATIC_URL = 'static/'

# CORS 設定（開発環境では全許可）
CORS_ALLOW_ALL_ORIGINS = True

# DRF 設定 (JWT 認証をデフォルトに)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
