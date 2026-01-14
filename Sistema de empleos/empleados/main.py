from servicios.gestion import mostrar_beneficio
from modelo.empleado import EmpleadoTiempoCompleto, EmpleadoMedioTiempo

empleado1 = EmpleadoTiempoCompleto("Ana", 1000, 5)
empleado2 = EmpleadoMedioTiempo("Carlos", 800, 2)

mostrar_beneficio(empleado1)
mostrar_beneficio(empleado2)
