import json
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth import login, authenticate, get_user
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
from .forms import *
from . import redis_client

class AuthView(View):

    def get(self, request):
        user = get_user(request)
        if user.is_authenticated:
            return redirect('map')
        data = {'form': LoginForm()}
        return render(request, 'registration/auth.html', context=data)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            form.clean()
            user = form.get_user()
            login(request, user)
            return redirect('map')
        else:
            return render(request, 'registration/auth.html', {
                'error_message': form.error_messages,
                'form': form
        })

class RegView(View):

    def get(self, request):
        user = get_user(request)
        if user.is_authenticated:
            return redirect('map')
        data = {'form': RegistrationForm()}
        return render(request, 'registration/reg.html', context=data)

    def post(self, request):
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.get_user()
            login(request, user)  # Автоматический вход после регистрации
            return redirect('map')  # Перенаправление на домашнюю страницу
        else:
            return render(request, 'registration/reg.html', context={
                'error_message': form.error_messages,
                'form': form
            })

class MapView(View):
    
    def get(self, request):
        data = {'map': Location.objects.get(pk=1)}
        
        return render(request, 'map/map.html', context=data)
    
    def post(self, request):
        data = {}
        user = get_user(request)
        if user.is_authenticated:
            request : HttpRequest = request
            mark = json.loads(request.body).get('mark')
            if not redis_client.setnx(f'rates:{user.id}', mark):
                pass

        return render(request, 'map/map.html', context=data)
    
    @method_decorator(login_required('', ''))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
