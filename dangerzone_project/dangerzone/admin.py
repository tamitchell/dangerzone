# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserProfileCreationForm, UserProfileChangeForm
from .models import News, UserProfile, Animals

# Register your models here.
class UserProfileAdmin(UserAdmin):
    add_form = UserProfileCreationForm
    form = UserProfileChangeForm
    model = UserProfile
    list_display = ['email', 'username', 'animal_list',]

admin.site.register([Animals, News])
admin.site.register(UserProfile, UserProfileAdmin)