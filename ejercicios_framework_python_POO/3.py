#Ejercicio 3
#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior.
#Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.
#Construye los siguientes métodos para la clase: Un constructor.
#Los setters y getters para el nuevo atributo.
#En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido()
#que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
#Además la retirada de dinero sólo se podrá hacer si el titular es válido.
#El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

# Clase Persona (necesaria para el titular)
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


# Clase CuentaJoven
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)  # Llamamos al constructor de la clase base
        self.__bonificacion = bonificacion  # Bonificación privada

    # Getter para la bonificación
    def get_bonificacion(self):
        return self.__bonificacion

    # Setter para la bonificación
    def set_bonificacion(self, bonificacion):
        if isinstance(bonificacion, (int, float)) and 0 <= bonificacion <= 100:
            self.__bonificacion = bonificacion
        else:
            print("Bonificación inválida. Debe estar entre 0 y 100.")

    # Método para verificar si el titular es válido
    def es_titular_valido(self):
        return 18 <= self.titular.get_edad() < 25

    # Método para retirar dinero
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)  # Usamos el método retirar de la clase base
        else:
            print("Retirada no permitida. Titular no válido para una Cuenta Joven.")

    # Método para mostrar los datos de la cuenta
    def mostrar(self):
        print(f"Cuenta Joven\nTitular: {self.titular}, Cantidad: {self.get_cantidad():.2f}, Bonificación: {self.__bonificacion:.2f}%")

# Crear un titular (Persona)
titular = Persona("Carlos", 20, "87654321B")

# Crear una CuentaJoven con ese titular
cuenta_joven = CuentaJoven(titular, cantidad=500.0, bonificacion=10.0)

# Mostrar los datos de la cuenta
cuenta_joven.mostrar()

# Intentar retirar dinero (titular válido)
print("\nIntentando retirar 200...")
cuenta_joven.retirar(200)
cuenta_joven.mostrar()

# Intentar retirar dinero con un titular no válido
titular_no_valido = Persona("Ana", 30, "12345678C")  # Titular mayor de 25 años
cuenta_no_valida = CuentaJoven(titular_no_valido, cantidad=300.0, bonificacion=5.0)

print("\nIntentando retirar 100 con titular no válido...")
cuenta_no_valida.retirar(100)
cuenta_no_valida.mostrar()

