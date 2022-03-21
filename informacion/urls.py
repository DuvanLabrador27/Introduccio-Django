from django.urls import path
from .views import InformacionView
app_name="blog"

urlpatterns= [
    path('',InformacionView.as_view(), name='home'),

]