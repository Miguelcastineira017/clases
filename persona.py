#crear una carpeta que se llame y adentro pone los
#archivos dino.py persona.py

# crear una clase persona(), en el archivo persona.py que tenga como atributos
#nombre, edad y profesion
#al instaciar la clase tiene que saludar igual que dino diciendo sus atributos

class Personal:

    def __init__(self, un_nombre="",un_edad="",un_profesion=""):
        self.nombre = un_nombre
        self.edad = un_edad
        self.profesion = un_profesion
        print("Mi nombre es", self.nombre, "tengo", self.edad, "y soy", self.profesion)
    
persona1 = Personal("Emilio", 30, "Doctor.")
persona2 = Personal("Jose", 40, "Cientifico.")
persona3 = Personal("Roberto", 50, "Astronauta.")
