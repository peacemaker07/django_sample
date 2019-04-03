from .base import *  # noqa
import django_heroku

DEBUG = False

django_heroku.settings(locals())
