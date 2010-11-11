from django.contrib import admin
from django.db.models import get_app, get_models

"""
Enables all models in app moxitems to be visible in the admin interface
"""
for model in get_models(get_app("moxitems")):
    admin.site.register(model)