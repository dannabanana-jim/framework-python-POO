#Ejercicio 2
#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales).
#El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
#Un constructor, donde los datos pueden estar vacíos.
#Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#mostrar(): Muestra los datos de la cuenta.
#ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

 # Clase Persona
class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

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

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Clase Cuenta
class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular  # El titular es obligatorio
        self.__cantidad = float(cantidad)  # Inicializamos la cantidad, no accesible directamente

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        if isinstance(titular, str) and titular:
            self.titular = titular
        else:
            print("Titular inválido")

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Titular: {self.titular}, Cantidad: {self.__cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        else:
            print("Cantidad a ingresar no válida")

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
        else:
            print("Cantidad a retirar no válida")



persona = Persona("Juan", 25, "12345678A")  # Crear un objeto Persona
cuenta = Cuenta(persona.get_nombre())  # Crear una cuenta con el nombre del titular

cuenta.mostrar()
cuenta.ingresar(100.50)
cuenta.mostrar()
cuenta.retirar(30)
cuenta.mostrar()
cuenta.retirar(100)
cuenta.mostrar()

