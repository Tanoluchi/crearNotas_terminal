import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Nota:

    def __init__(self, usuario_id, titulo, descripcion):
        self.__setUsuarioID(usuario_id)
        self.__setTitulo(titulo)
        self.__setDescripcion(descripcion)

    def __setUsuarioID(self, p_usuarioID):
        self.usuario_id = p_usuarioID
    def __setTitulo(self, p_titulo):
        self.titulo = p_titulo
    def __setDescripcion(self, p_descripcion):
        self.descripcion = p_descripcion
    

    def getUsuarioID(self):
        return self.usuario_id
    def getTitulo(self):
        return self.titulo
    def getDescripcion(self):
        return self.descripcion

    # Guardar en la base de datos
    def guardar(self):
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.getUsuarioID(), self.getTitulo(), self.getDescripcion())

        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]
    