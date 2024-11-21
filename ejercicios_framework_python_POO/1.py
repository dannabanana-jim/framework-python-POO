#Ejercicio 1
#Vamos a crear una clase llamada Persona. Sus atributos son: ,  y . Construye los siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#mostrar(): Muestra los datos de la persona.
#esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.



class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Getters y setters
    def set_nombre(self, nombre):
        if isinstance(nombre, str) and nombre:
            self.nombre = nombre
        else:
            print("Nombre inválido")

    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.edad = edad
        else:
            print("Edad inválida")

    def get_edad(self):
        return self.edad

    def set_dni(self, dni):
        if isinstance(dni, str) and dni:
            self.dni = dni
        else:
            print("DNI inválido")

    def get_dni(self):
        return self.dni

    # Métodos adicionales
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Ejemplo de uso
persona = Persona()
persona.set_nombre("Leoncio")
persona.set_edad(25)
persona.set_dni("12345678A")
persona.mostrar()
print("¿Es mayor de edad?", persona.es_mayor_de_edad())





















