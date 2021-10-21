from _typeshed import NoneType
from usuarios import usuario as modelo
class Acciones:

    def registro(self):
        print("\nOK, Vamos a registrarte en el sistema....")
        nombre = input("Cual es tu nombre?: ")
        apellido = input("Cual es tu apellido?: ")
        email = input("Introduce tu email: ")
        password = input("Introduzca una contraseña: ")
        # Creamos un usuario
        usuario = modelo.Usuario(nombre, apellido, email, password)
        # Lo registramos en la base de datos
        registro = usuario.registrar()
        # Hacemos una verificacion en el modulo usuario, si el indice cero del return
        # del metodo registrar es igual o mayor a 1 significa que se registro al usuario.
        if registro[0] >= 1:
            print(f"\nPerfecto {registro[1].nomYApe()}, te has registrado correctamente con el email {registro[1].getEmail()}")
        else:
            print("\nNo se ha podido registrar correctamente.")
    def login(self):
        print("\nOK, Identificate en el sistema....")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduzca su contraseña: ")

            usuario = modelo.Usuario('','', email, password)
            login = usuario.identificar()
            # Comprobamos si el email es igual que el email que me devuelve la consulta.
            if email == login[3]:
                print(f'Bienvenido {login[1]}, te has logeado correctamente en la fecha {login[5]}')
                self.proximasAcciones(login)
        except Exception as e:
            # print(type(e))
            # print(type.e.__name__)
            print(f"Login incorrecto, intentalo de nuevo.")

    def proximasAcciones(self, usuario):
        print("""
        Acciones Disponibles:
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input('\n¿Que quieres hacer?: ')

        if accion == "crear":
            print("\nOkay, vamos a crear una nota.")
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("\nLista de notas: ")
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("\nVamos a eliminar una nota")
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Hasta luego {usuario[1]}")
            exit()
        else:
            print(f"No se reconoce esa accion, intentalo de nuevo.")
            self.proximasAcciones(usuario)

