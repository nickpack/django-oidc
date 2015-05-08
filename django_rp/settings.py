# Django settings for access_web project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

BASE_ROOT = ""

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, r'db.sqlite'),  # Or path to database file if using sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '%s/static/' % BASE_ROOT

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '%s/static/admin/' % BASE_ROOT

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '9uqo5d00h-l0a45!a6fq*e$y+lxw3&^34-#%18z4ci5^s1t3=o'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'djangooidc.middleware.OpenIdMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
# CACHES = {
# 'default': {
# 'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
# }
#}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'djangooidc.backends.OpenIdUserBackend',
)

LOGIN_URL = 'openid'

ROOT_URLCONF = 'django_rp.urls'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "django_rp/templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',

    'djangooidc',
    'testapp',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'oic': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'djangooidc': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

###############################################################################
## PyOIDC specific settings

PORT = 8000
BASE = "http://localhost:%s/%s/marsu" % (PORT, BASE_ROOT) + "/"

# If BASE is https these have to be specified (.cer)
SERVER_KEY = ''
SERVER_CERT = ''
CA_BUNDLE = None
VERIFY_SSL = True

# information used when registering the client, this may be the same for all OPs
ME = {
    "application_type": "web",
    "contacts": ["ops@example.com"],
    "redirect_uris": ["%sauthz_cb" % BASE],
    "post_logout_redirect_uris": ["%slogout" % BASE]
}

BEHAVIOUR = {
    "response_type": "code",
    "scope": ["openid", "profile", "email", "address", "phone"],
}

# The keys in this dictionary are the OPs (OpenID Providers) short user friendly name
# not the issuer (iss) name.

CLIENTS = {
    # The ones that support webfinger, OP discovery and client registration
    # This is the default, any client that is not listed here is expected to
    # support dynamic discovery and registration.
    "": {
        "client_info": ME,
        "behaviour": BEHAVIOUR
    },
    "azuread": {
        "srv_discovery_url": "https://sts.windows.net/9019caa7-f3ba-4261-8b4f-9162bdbe8cd1/",
        "behaviour": BEHAVIOUR,
        "client_registration": {
             "client_id": "0d21f6d8-796f-4879-a2e1-314ddfcfb737",
             "client_secret": "6hzvhNTsHPvTiUH/GUHVsFDt8b0BajZNox/iFI7iVJ8=",
             "redirect_uris": ["http://localhost:8000/openid/authz_cb/"],
             "post_logout_redirect_uris": ["http://localhost:8000/unprotected"],
         }
    },
    # No webfinger support, but OP information lookup and client registration
    # "xenosmilus": {
    #     "srv_discovery_url": "https://xenosmilus2.umdc.umu.se:8091/",
    #     "client_info": ME,
    #     "behaviour": BEHAVIOUR
    # },
    # # Supports OP information lookup but not client registration
    # "op.example.org": {
    #     "srv_discovery_url": "https://example.org/op/discovery_endpoint",
    #     "client_registration": {
    #         "client_id": "abcdefgh",
    #         "client_secret": "123456789",
    #         "redirect_uris": ["https://rp.example.com/authn_cb"],
    #     }
    # },
    # # Does not support OP information lookup but dynamic client registration
    # "noop.example.com": {
    #     "provider_info": {
    #         "issuer": "",
    #         "authorization_endpoint": "",
    #         "token_endpoint": "",
    #         "userinfo_endpoint": "",
    #         "registration_endpoint": "",
    #         "jwks_uri": "",
    #         "scopes_supported": "",
    #         "response_types_supported": "",
    #         "subject_types_supported": "",
    #         "id_token_signing_alg_values_supported": "",
    #         "claims_supported": "",
    #     },
    #     "client_info": ME,
    # },
    # # Does not support any dynamic functionality
    # "nodyn.example.com": {
    #     "provider_info": {
    #         "issuer": "",
    #         "authorization_endpoint": "",
    #         "token_endpoint": "",
    #         "userinfo_endpoint": "",
    #         "registration_endpoint": "",
    #         "jwks_uri": "",
    #         "scopes_supported": "",
    #         "response_types_supported": "",
    #         "subject_types_supported": "",
    #         "id_token_signing_alg_values_supported": "",
    #         "claims_supported": "",
    #     },
    #     "client_registration": {
    #         "client_id": "abcdefg",
    #         "client_secret": "123456789",
    #         "redirect_uris": ["https://rp.example.com/authn_cb"],
    #     }
    # },
}
##
###############################################################################