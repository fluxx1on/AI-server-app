from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class AuthView(View):

    def get(self, request):
        data = {}
        
        return render(request, 'auth.html', context=data)

    def post(self, request):
        data = {}
        
        return render(request, 'auth.html', context=data)


class MapView(View):
    
    def get(self, request):
        data = {}
        
        return render(request, 'map.html', context=data)
    
    def post(self, request):
        data = {}
        
        return render(request, 'map.html', context=data)
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
