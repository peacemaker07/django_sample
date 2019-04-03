from .base import *  # noqa
import django_heroku

DEBUG = True

django_heroku.settings(locals())
