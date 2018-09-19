# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserProfileCreationForm
from .models import Animals
import requests
import json
from pprint import pprint

# Create your views here.
class SignUp(generic.CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def news_list(request):
    url = ('https://newsapi.org/v2/everything?'
        'q=science&'
        'from=2018-09-19&'
        'sortBy=popularity&'
        'apiKey=52ee4ff1d0d54903ae3442d5820c69fd')

    response = requests.get(url)
    readable_content = response.json()
    list_of_articles = readable_content['articles']

    index = 0
    while index < len(list_of_articles):
        for value in list_of_articles[index]:
            articles = list_of_articles[index][value]
        return articles
        index += 1

    return render(request, 'home.html', {'articles': articles})

def animal_list(request):
    animals = Animals.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})