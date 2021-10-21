import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:

    def __init__(self, nombre, apellido, email, password):
        self.__setNombre(nombre)
        self.__setApellido(apellido)
        self.__setEmail(email)
        self.__setPassword(password)

    def __setNombre(self, p_nombre):
        self.nombre = p_nombre
    def __setApellido(self, p_apellido):
        self.apellido = p_apellido
    def __setEmail(self, p_email):
        self.email = p_email
    def __setPassword(self, p_password):
        self.password = p_password

    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getEmail(self):
        return self.email
    def getPassword(self):
        return self.password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Cifrar contraseña, actualizamos la variable que contiene el objeto para cifrar a sha256
        # dentro le pasamos la contraseña (esta en String asi que...) utilizamos el metodo encode,
        # para pasar el string a bits.
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(NULL, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)
        # Pasamos la consulta (sql) y los datos que lo van a sustituir (usuario)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result

    def identificar(self):
        # Consulta para comprobar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Ciframos contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
        
    def nomYApe(self):
        return f"{self.getNombre()}, {self.getApellido()}"