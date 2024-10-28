from django.urls import path
from . import views
# . operator means same folder

urlpatterns =[
    #load page of the app will be sent to 'index.html' file
    path("", views.index, name='index')
]