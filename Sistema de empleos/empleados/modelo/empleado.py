# Clase base
class Empleado:
    def __init__(self, nombre, salario, anios_experiencia):
        # Encapsulación: atributos privados
        self.__nombre = nombre
        self.__salario = salario
        self.__anios_experiencia = anios_experiencia

    def calcular_beneficio(self):
        """
        Método polimórfico que será sobrescrito
        por las clases derivadas
        """
        return 0

    # Métodos getter
    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    def get_anios_experiencia(self):
        return self.__anios_experiencia


# Clase derivada
class EmpleadoTiempoCompleto(Empleado):
    def calcular_beneficio(self):
        # Beneficio basado en experiencia
        return self.get_salario() * (0.10 + 0.02 * self.get_anios_experiencia())


# Clase derivada
class EmpleadoMedioTiempo(Empleado):
    def calcular_beneficio(self):
        # Beneficio menor que tiempo completo
        return self.get_salario() * (0.05 + 0.01 * self.get_anios_experiencia())
