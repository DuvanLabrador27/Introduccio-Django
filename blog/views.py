from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class BlogList(View):
    def get(self, request, *args, **kwargs):
        contexto={
            
        }
        return render(request, 'blogList.html', contexto)