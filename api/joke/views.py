from django.shortcuts import render, redirect
from .forms import JokeForm
from .models import Joke
from django.core import serializers
from django.http import JsonResponse, HttpResponse
import json
import random
# Create your views here.

def home(request):
    form = JokeForm()
    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'home.html', context)


def random_page(request):
    random_joke = random.choice(Joke.objects.all())
    jokes_list = serializers.serialize('json', [random_joke])
    return HttpResponse(jokes_list, content_type="text/json-comment-filtered")