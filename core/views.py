
from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        #El render toma un objeto request, el template y un diccionario
        return render(request, 'index.html ', {})