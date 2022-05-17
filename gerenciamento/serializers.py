from rest_framework import serializers 
from gerenciamento.models import Curso, Professor, titulos, Bancas, Temas, TiposTcc, Equipe, Aluno, AreaConhecimento, LinhaPesquisa, EstruturaTCC, AcompanhamentoTcc, Devolutiva
from django.contrib.auth.models import User

from contas.serializers import UserSerializer



# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id','nome')

class titulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = titulos
        fields = ('id','nome')

class AreaConhecimento(serializers.ModelSerializer):
    class Meta: 
        model = AreaConhecimento
        fields = ('id', 'descricao')

class LinhaPesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinhaPesquisa
        fields= ('id', 'nome', 'areaConhecimento')
        dept = 1

class ProfessorSerializer(serializers.ModelSerializer):
    curso = CursosSerializer()
    linhaPesquisa = LinhaPesquisaSerializer()
    titulo = titulosSerializer(many=True)
    
    class Meta:
        model = Professor
        fields = ('id','nome', 'email', 'curso', 'titulo', 'linhaPesquisa')
        depth = 1


class TemasSerializer(serializers.ModelSerializer):
    orientador = ProfessorSerializer()

    class Meta:
        model = Temas
        fields = ('id','nome', 'orientador')
        depth = 1

class TiposTccSerializer(serializers.ModelSerializer):
    class Meta:
        model = TiposTcc
        fields = ('id','nome')

class EstruturaTCCSerializer(serializers.ModelSerializer):
    tipotcc = TiposTccSerializer()

    class Meta:
        model = EstruturaTCC
        fields = ('id', 'descricao', 'tipotcc')

class EquipesSerializer(serializers.ModelSerializer):
    tema = TemasSerializer()
    tipo = TiposTccSerializer()
    orientador = ProfessorSerializer()

    class Meta:
        model = Equipe
        fields = ('id','tema', 'tipo', 'orientador')

class AcompanhamentoTccSerializer(serializers.ModelSerializer):
    equipe = EquipesSerializer()
    etapa = EstruturaTCCSerializer()

    class Meta:
        model = AcompanhamentoTcc
        fields = ('id', 'status', 'texto', 'equipe', 'etapa')

class DevolutivaSerializer(serializers.ModelSerializer):
    acompanhamento = AcompanhamentoTccSerializer()
    
    class Meta:
        model = Devolutiva
        fields = ('id', 'descricao','acompanhamento')

class BancasSerializer(serializers.ModelSerializer):
    professores = ProfessorSerializer(many=True)
    equipe = EquipesSerializer()

    class Meta:
        model = Bancas
        fields = ('id','professores', 'equipe', 'data', 'ordemapresentacao')

class AlunosSerializer(serializers.ModelSerializer):
    curso = CursosSerializer()
    equipe = EquipesSerializer()    
    usuario = UserSerializer()
    
    class Meta:
        model = Aluno
        fields = ('id','nome', 'matricula', 'curso', 'equipe', 'usuario')
        depth = 1