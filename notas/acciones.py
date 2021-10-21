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
        return True
    def eliminar(self, usuario):
        return True
