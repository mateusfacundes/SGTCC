from django.shortcuts import render
from django.http.response import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.authtoken.serializers import AuthTokenSerializer


from gerenciamento.models import Curso, Professor, titulos, Bancas, Temas, TiposTcc, Equipe, Aluno
from gerenciamento.serializers import  UserSerializer, CursosSerializer, titulosSerializer, ProfessorSerializer, BancasSerializer, TemasSerializer, TiposTccSerializer, EquipesSerializer, AlunosSerializer

from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

#----------------------------Cursos------------------------------------------------------

#Mostrar todos 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarCursos(request,  format=None):
    curso = Curso.objects.all()
    curso_srl = CursosSerializer(curso, many=True)
    return JsonResponse(curso_srl.data, safe=False)

#Adcionar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def adicionarCurso(request):
    curso_data = JSONParser().parse(request)
    curso_srl = CursosSerializer(data = curso_data)
    if curso_srl.is_valid():
        curso_srl.save()
        return JsonResponse('Curso adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Curso', safe=False)

#Mostrar filtrado por ID
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarCurso(request, rid):
    curso = Curso.objects.get(id = rid)
    curso_srl = CursosSerializer(curso, many=False)
    return JsonResponse(curso_srl.data, safe=False)

#Atualizar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def atualizarCurso(request, rid):
    curso_data = JSONParser().parse(request)
    curso = Curso.objects.get(id = rid)
    curso_srl = CursosSerializer(curso, data = curso_data,  partial=True)
    if curso_srl.is_valid():
        curso_srl.save()
        return JsonResponse("Curso atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Atualizar Curso", safe=False)

#Deletar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deletarCurso(request, rid):
    curso = Curso.objects.get(inventario_id = rid)
    curso.delete()
    return JsonResponse("Curso deletado com sucesso", safe=False)

#----------------------------titulos------------------------------------------------------

#Mostrar todos 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarTitulos(request):
    titulos_data = titulos.objects.all()
    titulos_srl = titulosSerializer(titulos_data, many=True)
    return JsonResponse(titulos_srl.data, safe=False)

#Adcionar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def adicionarTitulo(request):
    titulos_data = JSONParser().parse(request)
    titulos_srl = titulosSerializer(data = titulos_data)
    if titulos_srl.is_valid():
        titulos_srl.save()
        return JsonResponse('Titulo adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Titulo', safe=False)

#Mostrar filtrado por ID
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarTitulo(request, rid):
    titulo = titulos.objects.get(id = rid)
    titulos_srl = titulosSerializer(titulo, many=False)
    return JsonResponse(titulos_srl.data, safe=False)

#Atualizar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def atualizarTitulo(request, rid):
    titulos_data = JSONParser().parse(request)
    titulo = titulos.objects.get(id = rid)
    titulos_srl = titulosSerializer(titulo, data = titulos_data,  partial=True)
    if titulos_srl.is_valid():
        titulos_srl.save()
        return JsonResponse("Titulo atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Atualizar Titulo", safe=False)

#Deletar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deletarTitulo(request, rid):
    titulo = titulos.objects.get(inventario_id = rid)
    titulo.delete()
    return JsonResponse("Titulo deletado com sucesso", safe=False)

#----------------------------Professores--------------------------------------------------

#Adcionar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def adicionarProfessor(request):
    professores_data = JSONParser().parse(request)
    professor_srl = ProfessorSerializer(data = professores_data)
    if professor_srl.is_valid():
        professor_srl.save()
        return JsonResponse('Professor adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Professor', safe=False)

#Mostrar todos 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarProfessores(request):
    professor_data = Professor.objects.all()
    professor_srl = ProfessorSerializer(professor_data, many=True)
    return JsonResponse(professor_srl.data, safe=False)

#Mostrar filtrado por ID
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarProfessor(request, rid):
    professor = Professor.objects.get(id = rid)
    professor_srl = ProfessorSerializer(professor, many=False)
    return JsonResponse(professor_srl.data, safe=False)

#Atualizar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def atualizarProfessor(request, rid):
    professor_data = JSONParser().parse(request)
    professor = Professor.objects.get(id = rid)
    professor_srl = ProfessorSerializer(professor, data = professor_data,  partial=True)
    if professor_srl.is_valid():
        professor_srl.save()
        return JsonResponse("Professor atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Atualizar Professor", safe=False)

#Deletar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deletarProfessore(request, rid):
    professor = Professor.objects.get(inventario_id = rid)
    professor.delete()
    return JsonResponse("Professor deletado com sucesso", safe=False)

#----------------------------Bancas--------------------------------------------------

#Adcionar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def adicionarBanca(request):
    banca_data = JSONParser().parse(request)
    banca_srl = BancasSerializer(data = banca_data)
    if banca_srl.is_valid():
        banca_srl.save()
        return JsonResponse('Banca adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Banca', safe=False)

#Mostrar todos 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarBancas(request):
    banca_data = Bancas.objects.all()
    banca_srl = BancasSerializer(banca_data, many=True)
    return JsonResponse(banca_srl.data, safe=False)

#Mostrar filtrado por ID
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarBanca(request, rid):
    banca = Bancas.objects.get(id = rid)
    banca_srl = BancasSerializer(banca, many=False)
    return JsonResponse(banca_srl.data, safe=False)

#Atualizar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def atualizarBanca(request, rid):
    banca_data = JSONParser().parse(request)
    banca = Bancas.objects.get(id = rid)
    banca_srl = BancasSerializer(banca, data = banca_data,  partial=True)
    if banca_srl.is_valid():
        banca_srl.save()
        return JsonResponse("Banca atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Atualizar Banca", safe=False)

#Deletar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deletarBanca(request, rid):
    banca = Bancas.objects.get(inventario_id = rid)
    banca.delete()
    return JsonResponse("Banca deletado com sucesso", safe=False)

#----------------------------Temas--------------------------------------------------

#Adcionar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def adicionarTemas(request):
    banca_data = JSONParser().parse(request)
    banca_srl = TemasSerializer(data = banca_data)
    if banca_srl.is_valid():
        banca_srl.save()
        return JsonResponse('Temas adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Temas', safe=False)

#Mostrar todos
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser]) 
def mostrarTemas(request):
    tema_data = Temas.objects.all()
    tema_srl = TemasSerializer(tema_data, many=True)
    return JsonResponse(tema_srl.data, safe=False)

#Mostrar filtrado por ID
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarTema(request, rid):
    tema = Temas.objects.get(id = rid)
    tema_srl_srl = TemasSerializer(tema, many=False)
    return JsonResponse(tema_srl_srl.data, safe=False)

#Atualizar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def atualizarTema(request, rid):
    tema_data = JSONParser().parse(request)
    tema = Temas.objects.get(id = rid)
    tema_srl = TemasSerializer(tema, data = tema_data,  partial=True)
    if tema_srl.is_valid():
        tema_srl.save()
        return JsonResponse("Temas atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Atualizar Temas", safe=False)

#Deletar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deletarTema(request, rid):
    tema = Temas.objects.get(inventario_id = rid)
    tema.delete()
    return JsonResponse("Temas deletado com sucesso", safe=False)

#----------------------------TiposTcc--------------------------------------------------

#Adcionar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def adicionarTipoTcc(request):
    tipotcc_data = JSONParser().parse(request)
    tipotcc_srl = TemasSerializer(data = tipotcc_data)
    if tipotcc_srl.is_valid():
        tipotcc_srl.save()
        return JsonResponse('TipoTcc adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Tipo Tcc', safe=False)

#Mostrar todos 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarTipoTccs(request):
    tipotcc_data = TiposTcc.objects.all()
    tipotcc_srl = TiposTccSerializer(tipotcc_data, many=True)
    return JsonResponse(tipotcc_srl.data, safe=False)

#Mostrar filtrado por ID
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarTipoTcc(request, rid):
    tipotcc = TiposTcc.objects.get(id = rid)
    tipotcc_srl = TiposTccSerializer(tipotcc, many=False)
    return JsonResponse(tipotcc_srl.data, safe=False)

#Atualizar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def atualizarTipoTcc(request, rid):
    tipotcc_data = JSONParser().parse(request)
    tipotcc = TiposTcc.objects.get(id = rid)
    tipotcc_srl = TiposTccSerializer(tipotcc, data = tipotcc_data,  partial=True)
    if tipotcc_srl.is_valid():
        tipotcc_srl.save()
        return JsonResponse("Tipo Tcc atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Atualizar Tipo Tcc", safe=False)

#Deletar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deletarTipoTcc(request, rid):
    tipotcc = TiposTcc.objects.get(inventario_id = rid)
    tipotcc.delete()
    return JsonResponse("Tipo Tcc deletado com sucesso", safe=False)

#----------------------------Equipe--------------------------------------------------

#Adcionar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def adicionarEquipe(request):
    equipe_data = JSONParser().parse(request)
    equipe_srl = TemasSerializer(data = equipe_data)
    if equipe_srl.is_valid():
        equipe_srl.save()
        return JsonResponse('Equipe adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Equipe', safe=False)

#Mostrar todos 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarEquipes(request):
    equipe_data = Equipe.objects.all()
    equipe_srl = EquipesSerializer(equipe_data, many=True)
    return JsonResponse(equipe_srl.data, safe=False)

#Mostrar filtrado por ID
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarEquipe(request, rid):
    equipe = Equipe.objects.get(id = rid)
    equipe_srl = EquipesSerializer(equipe, many=False)
    return JsonResponse(equipe_srl.data, safe=False)

#Atualizar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def atualizarEquipe(request, rid):
    tipotcc_data = JSONParser().parse(request)
    equipe = Equipe.objects.get(id = rid)
    equipe_srl = EquipesSerializer(equipe, data = tipotcc_data,  partial=True)
    if equipe_srl.is_valid():
        equipe_srl.save()
        return JsonResponse("Equipe atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Atualizar Equipe", safe=False)

#Deletar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deletarEquipe(request, rid):
    equipe = Equipe.objects.get(inventario_id = rid)
    equipe.delete()
    return JsonResponse("Equipe deletado com sucesso", safe=False)


#----------------------------Aluno--------------------------------------------------

#Adcionar
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def adicionarAluno(request):
    aluno_data = JSONParser().parse(request)
    aluno_srl = AlunosSerializer(data = aluno_data)
    if aluno_srl.is_valid():
        aluno_srl.save()
        return JsonResponse('Aluno adicionado com sucesso!', safe=False)
    return JsonResponse('Falha ao Adicionado Aluno', safe=False)

#Mostrar todos 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarAlunos(request):
    aluno_data = Aluno.objects.all()
    aluno_srl = AlunosSerializer(aluno_data, many=True)
    return JsonResponse(aluno_srl.data, safe=False)

#Mostrar filtrado por ID
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def mostrarAluno(request, rid):
    aluno = Aluno.objects.get(id = rid)
    aluno_srl = AlunosSerializer(aluno, many=False)
    return JsonResponse(aluno_srl.data, safe=False)

#Atualizar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def atualizarAluno(request, rid):
    aluno_data = JSONParser().parse(request)
    aluno = Aluno.objects.get(id = rid)
    aluno_srl = AlunosSerializer(aluno, data = aluno_data,  partial=True)
    if aluno_srl.is_valid():
        aluno_srl.save()
        return JsonResponse("Aluno atualizado com sucesso!", safe=False)
    return JsonResponse("Falha ao Atualizar Aluno", safe=False)

#Deletar 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def deletarAluno(request, rid):
    aluno = Aluno.objects.get(inventario_id = rid)
    aluno.delete()
    return JsonResponse("Aluno deletado com sucesso", safe=False)