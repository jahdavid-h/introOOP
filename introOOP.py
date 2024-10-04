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
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"{self.nombre} ahora trabaja como {self.ocupacion}.")

    def saludar(self, otra_persona):
        print(f"{self.nombre} te manda a saludar {otra_persona.nombre}.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}, Ocupación: {self.ocupacion}")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 23, "Masculino", "Estudiente")
persona2 = Persona("Victor", 10, "Masculino", "Estudiante")
persona3 = Persona("David", 19, "Masculino", "Estudante")

# Usar los métodos de la clase
print("\n")
persona1.presentarse()
persona1.cumplir_anios()
persona1.cambiar_ocupacion("Docente")
persona1.mostrar_info()
persona1.saludar(persona2)
print("\n")

persona2.presentarse()
persona2.cumplir_anios()
persona2.cambiar_ocupacion("Maestro")
persona2.mostrar_info()
persona2.saludar(persona3)
print("\n")

persona3.presentarse()
persona3.cumplir_anios()
persona3.cambiar_ocupacion("Ingeniero")
persona3.mostrar_info()
persona3.saludar(persona1)
