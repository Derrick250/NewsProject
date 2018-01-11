from .base import *




SECRET_KEY = env('DJANGO_SECRET_KEY', default='^ak9md7o=e*3ifr9m1c&qp-bcetc(&t2cr)rnfa^a52lym&!gz')

DEBUG = env.bool('DJANGO_DEBUG', True)
