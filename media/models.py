from django.db import models


# Create your models here.
class Picture(models.Model):
    nome = models.CharField(max_length=100)
    designer = models.CharField(max_length=200, default='')
    ano = models.IntegerField(null=True, verbose_name='Ano de criação')
    pais = models.CharField(max_length=50, default='', verbose_name='País')
    website_oficial = models.URLField(null=True)
    imagem = models.ImageField(upload_to='pictures/')

    def __str__(self):
        return self.nome