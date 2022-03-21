from django.urls import path
from .views import amazonView
app_name="amazon"

urlpatterns= [
    path('',amazonView.as_view(), name='home'),

]