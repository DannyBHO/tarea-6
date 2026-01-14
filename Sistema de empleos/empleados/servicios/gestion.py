def mostrar_beneficio(empleado):
    """
    Función que recibe un objeto Empleado
    y aplica polimorfismo
    """
    print(f"Empleado: {empleado.get_nombre()}")
    print(f"Beneficio: ${empleado.calcular_beneficio():.2f}")
