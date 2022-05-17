from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from gerenciamento.models import Aluno, Equipe, Curso
from gerenciamento.serializers import AlunosSerializer

from rest_framework.parsers import JSONParser

from contas.serializers import UserSerializer, TokenSerializer
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

UserModel = get_user_model()

@api_view(['POST'])
def registration_view(request):
	data = {}

	register_data = JSONParser().parse(request)
	aluno_data = register_data.pop('aluno')

	
	registro_srl = UserSerializer(data=register_data)
	

	if registro_srl.is_valid() :
		account = registro_srl.save()

		curso1 = Curso.objects.get(pk=aluno_data['curso'])
		equipe1 = Equipe.objects.get(pk=aluno_data['equipe'])

		Aluno.objects.create(nome=aluno_data['nome'], matricula=aluno_data['matricula'], curso=curso1, equipe=equipe1, usuario=account)
		
		data['response'] = 'successfully registered new user.'
		data['email'] = account.email
		data['username'] = account.username
		data['matricula'] = aluno_data['matricula']
		token = Token.objects.create(user=account)
		data['token'] = str(token)

	else:
		data = registro_srl.errors

	return Response(data)

@api_view(['POST'])
def login_view(request):
	data = {}

	serizlizer = UserSerializer(data=request.data)
	serizlizer.is_valid()
	user_info = serizlizer.data

	user = UserModel.objects.get(username=user_info['username'])
	
	if user.is_authenticated:
		data['response'] = 'logado com sucecsso'
		data['username'] = user.username
		data['email'] = user.email
		token = Token.objects.get_or_create(user=user)
		print( token[0])
		data['token'] = str(token[0])
	else:
		data['response'] = 'Falha ao logar'

	return Response(data) 
	

@api_view(['GET'])
def logout_view(request):
	request.user.auth_token.delete()
	return Response(status=status.HTTP_200_OK)