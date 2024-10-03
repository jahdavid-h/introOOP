# Definir la clase Persona
class Persona:
    def __init__(self, nombre, edad, genero, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.ocupacion = ocupacion

    # Métodos de la clase Persona
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ha cumplido años y ahora tiene {self.edad} años.")

    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"{self.nombre} ahora trabaja como {self.ocupacion}.")

    def saludar(self, otra_persona):
        print(f"{self.nombre} saluda a {otra_persona.nombre}.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Ocupación: {self.ocupacion}")

    def mandar_saludo(self, nombreOtra):
        print(f"Hola {self.nombre} saluda a {nombreOtra.nombre}")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 19, "Masculino", "Estudiente")

# Usar los métodos de la clase
persona1.presentarse()
persona1.cumplir_anios()
persona1.cambiar_ocupacion("Profesor")
persona1.mostrar_info()

# Crear otra instancia para demostrar el método saludar
persona2 = Persona("Victor", 10, "Masculino", "Estudiante")
persona1.saludar(persona2)
persona2.mandar_saludo(persona1)

persona3 = Persona("Victor", 10, "Masculino", "Ingeniero")
persona1.saludar(persona3)
