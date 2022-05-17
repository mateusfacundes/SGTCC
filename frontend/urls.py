from django.urls import path
from frontend import views

urlpatterns = [
    path('', views.loginFront),
    path('registro', views.register),
    path('cursos', views.cursos_view),
    
]