from django.db import models

class Artista(models.Model):
	NACIONALIDADE = (
			('ALE', 'Alemanha'),
			('ARG', 'Argentina'),
			('BRA', 'Brasil'),
			('CAN', 'Canadá'),
			('ESP', 'Espanha'),
			('EUA', 'Estados Unidos'),
			('FRA', 'França'),
			('ING', 'Inglaterra'),
			('ITA', 'Itália'),
			('NOR', 'Noruega'),
		)
	nome = models.CharField(max_length=100)
	nacionalidade = models.CharField(max_length=3, choices=NACIONALIDADE)
	genero = models.CharField(max_length=50)
	telefone = models.CharField(max_length=9)

	def __str__(self):
		return self.nome

class Musica(models.Model):
	nome = models.CharField(max_length=100)
	duracao = models.DurationField()

	def __str__(self):
		return self.nome

class Album(models.Model):
	nome = models.CharField(max_length=100)
	ano = models.CharField(max_length=4)
	artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
	musicas = models.ManyToManyField(Musica)

	def __str__(self):
		return self.nome

