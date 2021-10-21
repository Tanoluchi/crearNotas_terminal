"""
- Abrir asistente
- Login y Registro
- Si elegimos registro, se creara un usuario en la base de datos
- Si elegimos login, identificara al usuario y luego preguntara que quiere hacer
- Crear nota, Mostrar notas o borrar nota.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

hazEl = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == "Registro" or accion == "registro":
    hazEl.registro()
elif accion == "Login" or accion == "login":
    hazEl.login()

