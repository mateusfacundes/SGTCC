from django.shortcuts import render

# Create your views here.
def loginFront(request):
    return render(request,'frontend/login.html')

def register(request):
    return render(request, 'frontend/register.html')


def cursos_view(request):
    return render(request,'frontend/show_cursos.html')