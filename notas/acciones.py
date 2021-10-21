import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f'\nOkay, {usuario[1]} vamos a crear una nueva nota')
        titulo = input('Introduce el titulo de tu nota: ')
        descripcion = input('Introduzca el contenido de la nota: ')

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f'Se ha guardado correctamente la nota con el titulo: {nota.getTitulo()}')
        else:
            print(f'No ha podido guardar la nota, lo siento {usuario[1]}')
    def mostrar(self, usuario):
        print(f'Okay, {usuario[1]} aqui tienes todas tus notas: ')

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("*****************")
            print(nota[2])
            print(nota[3])
            print("*****************")
    def eliminar(self, usuario):
        print(f'Okay, {usuario[1]} vamos a borrar una nota!')

        titulo = input("Ingrese el titulo de la nota a borrar: ")
        
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f'Hemos borrado la nota {nota.getTitulo()}')
        else:
            print('Ha ocurrido un error, no se ha podido borrar la nota. Intentalo de nuevo!')
