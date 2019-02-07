#crear una carpeta que se llame y adentro pone los
#archivos dino.py persona.py

# crear una clase persona(), en el archivo persona.py que tenga como atributos
#nombre, edad y profesion
#al instaciar la clase tiene que saludar igual que dino diciendo sus atributos

class Personal:

    def __init__(self, un_nombre=" ", un_edad="", un_profesion=" "):
        self.nombre = un_nombre
        self.edad = un_edad
        self.profesion = un_profesion
        print("Mi nombre es", self.nombre, "tengo", self.edad, "y soy", self.profesion)

    def cumpleanhos(self):
        self.edad = self.edad + 1
        print(self.edad)
    
persona1 = Personal("Emilio", 33, "Doctor.")
persona2 = Personal("Jose", 48, "Cientifico.")
persona3 = Personal("Roberto", 51, "Astronauta.")

# Agregar un metodo(self)a la clase persona, que se llame cumpleanhos
# y aumente la edad de la persona en un anho y retorna la edad

persona1.cumpleanhos()
persona2.cumpleanhos()
persona3.cumpleanhos()