#coding: utf-8          ### Obsleto para Python3
######################################################################
### Programacao Orientada a Objetos - UNIS - Ciclo 2
### Amanda Pavanelli - Salvador, BA, Brasil - Maio/2021
### Primeiro programa sobre classes: Guitarra.py    
######################################################################
### Definindo a classe Guitarra
class Guitarra:
    def __init__(self, serie, fabrica, modelo, tipo, madeira, valor):
        self.serie = serie
        self.fabrica = fabrica
        self.modelo = modelo
        self.tipo = tipo
        self.madeira = madeira
        self.valor = valor

### Definindo a minha guitarra - De verdade!!! 
MyGuitar = Guitarra(17423,               ## Numero de serie
                    "Gibson",               ## Fabricante
                    "Les Paul",             ## Modelo da guitarra
                    "Elétrica",             ## Tipo
                    "Mogno",                ## Madeira usada
                    28000)                  ## Valor em reais

### Apresentando as principais caracteristicas da minha guitarra
print("\nCaracteristicas da minha super guitarra:\n")
print("Numero de série = ", MyGuitar.serie) 
print("Madeira usada na manufatura:", MyGuitar.madeira)
print("Preço da guitarra = R$", MyGuitar.valor, ",00")
print("Tipo da minha guitarra:", MyGuitar.tipo)

######################################################################
print("\nAtividade concluida!\n")
### FIM
