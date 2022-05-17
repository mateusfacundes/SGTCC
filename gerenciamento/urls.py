from django.urls import path, include 
from django.http import HttpResponse
from gerenciamento import views

urlpatterns = [

    #Chamada CRUD Cursos
    path('adicionarcursos/', views.mostrarCursos),
    path('cursos/', views.mostrarCursos),
    path('curso/<str:rid>/', views.mostrarCurso),
    path('atualizarcurso/<str:rid>/', views.deletarCurso),
    path('deletarcurso/<str:rid>/', views.deletarCurso),

    #Chamada CRUD Titulos
    path('adicionartitulos/', views.adicionarTitulo),
    path('titulos/', views.mostrarTitulos),
    path('titulo/<str:rid>/', views.mostrarTitulo),
    path('atualizartitulo/<str:rid>/', views.atualizarTitulo),
    path('deletartitulo/<str:rid>/', views.deletarTitulo),

    #Chamada CRUD Professor
    path('adicionarprofessor/', views.adicionarProfessor),
    path('professores/', views.mostrarProfessores),
    path('professor/<str:rid>/', views.mostrarProfessor),
    path('atualizarprofessor/<str:rid>/', views.atualizarProfessor),
    path('deletarprofessor/<str:rid>/', views.deletarProfessore),

    #Chamada CRUD Bancas
    path('adicionarbancas/', views.adicionarBanca),
    path('bancas/', views.mostrarBancas),
    path('banca/<str:rid>/', views.mostrarBanca),
    path('atualizarbancas/<str:rid>/', views.atualizarBanca),
    path('deletarbancas/<str:rid>/', views.deletarBanca),

    #Chamada CRUD TiposTcc
    path('adicionartipotcc/', views.adicionarTipoTcc),
    path('tipotccs/', views.mostrarTipoTccs),
    path('tipotcc/<str:rid>/', views.mostrarTipoTcc),
    path('atualizartipotcc/<str:rid>/', views.atualizarTipoTcc),
    path('deletartipotcc/<str:rid>/', views.deletarTipoTcc),

    #Chamada CRUD Equipe
    path('adicionarequipe/', views.adicionarEquipe),
    path('equipes/', views.mostrarEquipes),
    path('equipe/<str:rid>/', views.mostrarEquipe),
    path('atualizarequipe/<str:rid>/', views.atualizarEquipe),
    path('deletarequipe/<str:rid>/', views.deletarEquipe),

    #Chamada CRUD Atulo
    path('adicionaraluno/', views.adicionarAluno),
    path('alunos/', views.mostrarAlunos),
    path('aluno/<str:rid>/', views.mostrarAluno),
    path('atualizaraluno/<str:rid>/', views.atualizarAluno),
    path('deletaraluno/<str:rid>/', views.deletarAluno),
]