from django.db import models

# Create your models here.
class Naipe(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class Instrumento(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nome}"
    
class Musico(models.Model):
    VOZES = {
        '1a': 'Primeira Voz',
        '2a': 'Segunda Voz',
        '3a': 'Terceira Voz',
    }
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField('nome do músico', max_length=100)
    data_nascimento = models.DateField(verbose_name='data de nascimento')
    data_ingresso = models.DateField(verbose_name='data de ingresso')
    naipe = models.ForeignKey(Naipe, on_delete=models.CASCADE)
    instrumento = models.ForeignKey(Instrumento, on_delete=models.CASCADE, verbose_name='instrumento do músico')
    voz = models.CharField("voz do instrumento", max_length=2, choices=VOZES.items())
    foto = models.ImageField(upload_to='img/musicos', null=True, blank=True)
    

    def __str__(self):
        return f"{self.nome}"
    
class Diretoria(models.Model):
    CARGOS = [
        ('PRES', 'Presidente'),
        ('VP', 'Vice-presidente'),
        ('TES', 'Tesoureiro'),
        ('VT', 'Vice-tesoureiro'),
        ('SEC', 'Secretário'),
        ('2SEC', 'Segundo secretário')
    ]

    cargo = models.CharField(max_length=4, choices=CARGOS)
    nome = models.CharField(max_length=100)
    contato = models.EmailField(null=True, blank=True)