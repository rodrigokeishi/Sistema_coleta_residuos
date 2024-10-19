from django.db import models

# Create your models here.




LISTA_CATEGORIAS = (
    ("GRANDES_EQUIPAMENTOS","Grandes Equipamentos"),
    ("PEQUENOS_EQUIPAMENTOS/ELETROPORTATEIS", "Pequenos Equipamentos ou Eletroportáteis"),
    ("EQUIPAMENTOS_INFORMATICA/TELEFONIA", "Equipamentos de Informática ou Telefonia"),
    ("PILHAS/BATERIAS", "Pilhas ou Baterias portáteis"),
)

# Criar o Residuo Eletronico
class Residuo(models.Model):
    produto = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_residuos')
    descricao = models.TextField(max_length=10000)
    categoria = models.CharField(max_length=50, choices=LISTA_CATEGORIAS)

    def __str__(self):
        return self.produto


# Criar a cadastro de empresas

# Criar os usuarios

