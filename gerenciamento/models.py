from django.db import models
from django.contrib.auth import get_user_model # If used custom user model
# Create your models here.
userModel = get_user_model()

class Curso(models.Model):
    nome = models.CharField(max_length=40)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class titulos(models.Model):
    nome = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    instituicao = models.CharField(max_length=40)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class AreaConhecimento(models.Model):
    descricao = models.CharField(max_length=40) 
    
    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class LinhaPesquisa(models.Model):
    nome = models.CharField(max_length=40)
    areaConhecimento = models.ForeignKey(AreaConhecimento, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class Professor(models.Model):
    nome = models.CharField(max_length=40)
    email = models.CharField(max_length=70)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    linhaPesquisa = models.ForeignKey(LinhaPesquisa, on_delete=models.CASCADE)
    titulo = models.ManyToManyField(titulos)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class Temas(models.Model):
    nome = models.CharField(max_length=40)
    orientador = models.ForeignKey(Professor, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class TiposTcc(models.Model):
    nome = models.CharField(max_length=40)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class EstruturaTCC(models.Model):
    descricao = models.CharField(max_length=40)
    tipotcc = models.ForeignKey(TiposTcc, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class Equipe(models.Model):
    tema = models.ForeignKey(Temas, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TiposTcc, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Professor, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class AcompanhamentoTcc(models.Model):
    status = models.CharField(max_length=20)
    texto = models.TextField()
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    etapa = models.ForeignKey(EstruturaTCC, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class Devolutiva(models.Model):
    descricao = models.TextField()
    acompanhamento = models.ForeignKey(AcompanhamentoTcc, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class Bancas(models.Model):
    professores = models.ManyToManyField(Professor)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    data = models.DateField()
    ordemapresentacao = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)

class Aluno(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipe, on_delete=models.CASCADE)
    usuario = models.ForeignKey(userModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updatad_at = models.DateTimeField(auto_now=True)


