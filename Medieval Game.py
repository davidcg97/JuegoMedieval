import random

class Ciudadanos:

    def __init__(self): # Constructor
        Granjeros.__init__(self)
        Artesanos.__init__(self)
        Militares.__init__(self)
        Taberneros.__init__(self)
        Curas.__init__(self)
        self.profesion = random.choice(profesion)
        self.cantidad = cantidad
        self.comida = 50
        cantidad = cantgranj + cantartes + cantmili + canttaber + cantcuras

    def __str__(self):
        return f"{self.profesion}, {self.cantidad}"

class Granjeros(Ciudadanos):

    def __init__(self): # Constructor
        Ciudadanos.__init__(self)
        self.profesion = "Granjero"
        self.cantgranj = cantgranj
    
    def Producir_comida(self):
        Ciudadanos.__init__(self)
        if comida > 0 and cantgranj > 10:
            comida += 1

    def Reproducir(self):
        Ciudadanos.__init__(self)
        Artesanos.__init__(self)
        if comida >= 10 and cantgranj + cantartes >= 20:
            random.choice(profesion)

    def __str__(self):
        return f"{self.cantgranj}"

class Artesanos(Ciudadanos):

    def __init__(self): # Constructor
        Ciudadanos.__init__(self)
        self.profesion = "Artesano"
        self.cantartes = cantartes
    
    def Producir_elementos(self):
        armas = ["Armadura", "Espada", "Escudo", "Lanza"]
        arma = random.choice(armas)
        return f"{arma}"

    def Reproducir(self):
        Ciudadanos.__init__(self)
        Granjeros.__init__(self)
        if comida >= 10 and cantgranj + cantartes >= 20:
            random.choice(profesion)

    def __str__(self):
        return f"{self.cantartes}"

class Militares:

    def __init__(self): # Constructor
        Ciudadanos.__init__(self)
        Artesanos.__init__(self)
        self.cantmili = cantmili
        self.arma = Artesanos.Producir_elementos()
        self.tipo = tipo
        if self.arma == "Armadura":
            tipo == "Armado"
        if self.arma == "Espada":
            tipo == "Guerrero"
        if self.arma == "Escudo":
            tipo == "Defensor"
        if self.arma == "Lanza":
            tipo == "Lancero"
    
    def Luchar(self):
        if self.tipo == "Armado":
            print("Vistoria.")
        elif self.tipo == "Guerrero":
            print("Vistoria.")
        elif self.tipo == "Defensor":
            print("Derrota.")
        elif self.tipo == "Lancero":
            print("Derrota.")

    #def Organizar(self):

    def __str__(self):
        return f"{self.cantmili}, {self.arma}, {self.tipo}"

class Taberneros:

    def __init__(self): # Constructor
        Ciudadanos.__init__(self)
        self.profesion = "Tabernero"
        self.canttaber = canttaber
        self.hidromiel = hidromiel
    
    def Producir_hidromiel(self):
        Ciudadanos.__init__(self)
        if comida > 20 and canttaber > 10:
            hidromiel += 1

    #def Dirigir(self):

    def __str__(self):
        return f"{self.canttaber}"

class Curas:

    def __init__(self): # Constructor
        Ciudadanos.__init__(self)
        self.profesion = "Cura"
        self.cantcuras = cantcuras
    
    #def Gastar(self):

    #def Defender(self):

    def __str__(self):
        return f"{self.cantcuras}"

profesion = ["Granjero", "Artesano", "Militar", "Tabernero", "Cura"]