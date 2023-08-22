from pathlib import Path
import os   
BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-70w6h-3g3!=$#qs4qst_e5vf-x*58)f6_hr##)*z*%yma7tawh'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'orders.apps.OrdersConfig',     
    'cart.apps.CartConfig',        
    'products.apps.ProductsConfig', 
    'e_app.apps.EAppConfig',        
    'payment.apps.PaymentConfig',   
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

ROOT_URLCONF = 'e_commerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'e_app/templates', BASE_DIR/'products/templates', BASE_DIR/'cart/templates', BASE_DIR/'orders/templates', BASE_DIR/'payment/templates'],
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

WSGI_APPLICATION = 'e_commerce.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = 'static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'e_app/static'),
    os.path.join(BASE_DIR, 'payment/static'),
    os.path.join(BASE_DIR, 'products/static'),
    os.path.join(BASE_DIR, 'cart/static'),
    os.path.join(BASE_DIR, 'orders/static'),
    
]
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

