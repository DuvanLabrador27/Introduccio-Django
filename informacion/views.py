from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class InformacionView(View):
    def get(self, request, *args, **kwargs):
        contexto={
            
        }
        return render(request, 'informacion.html', contexto)