from datetime import datetime
from django.db import models

# Create your models here.
class Projeto(models.Model):
    """
    Classe para mdelar e criar bando de dados para meu app
    """
    nome_projeto = models.CharField(max_length=200)
    descricao_projeto = models.TextField()
    cliente = models. CharField(max_length=100)
    data_conclusao = models.DateTimeField(default=datetime.now, blank=True)
    website = models.CharField(max_length=200)
    linguagem = models.CharField(max_length=50)
    tags_projeto = models.TextField()
    detalhes_pprojeto = models.TextField()
