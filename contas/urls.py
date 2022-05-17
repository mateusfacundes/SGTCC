from django.urls import path
from contas.views import registration_view, logout_view, login_view

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),
	path('login', login_view, name="login"),
	path('logout', logout_view, name="login"),
]

