#2do ejercicio
class Dino:

    def __init__(self,nombre,color,edad):
        print("Hola soy un dinosaurio", nombre, "y soy de color", color, "y naci", edad, "b.C.")

pepito = Dino("Pepe", "verde moco", 135)

#3er ejercicio  
class Dino:
    def __init__(self,un_nombre=" ",un_color=" "):
        self.nombre = un_nombre
        self.color = un_color
        print("Hola soy un dinosaurio, me llamo", self.nombre,"y soy de color", self.color)

pepito1 = Dino("Pepe", "azul")
pepito2 = Dino("Pepo", "rojo")
pepito3 = Dino("Pepx", "rosa")


#4to ejercicio  
class Dino:
    def __init__(self,un_nombre="",un_color=""):
        self.nombre = un_nombre
        self.color = un_color
        print("Hola soy un dinosaurio, me llamo", self.nombre,"y soy de color", self.color)

    def rugir(self,rugido):
        #print(self)
        #print(rugido)
        print("RRRRWWAAAR!!!", rugido)

    def cambiar_color(self, un_color):
        self.color= un_color

pepito = Dino("Pepe", "azul")

pepito.cambiar_color("Lila")

pepito.rugir("AHHHHHHH!!!!!!!!")

pepito1 = Dino("Pepu", "naranaja")
pepito2 = Dino("Pepo", "rojo")
pepito3 = Dino("Pepx", "rosa")
