class Gimnasio:
    def __init__(self, id, nombre, capacidad):
        self.id = id
        self.nombre = nombre
        self.capacidad = capacidad
        self.usuarios = []

    def anyadirUsuario(self, Usuario):
            self.usuarios.append(Usuario)

    def consultarUsuarios(self):
        for usuario in self.usuarios:
            print(usuario.nombre)
        return self.usuarios

    def contarUsuarios(self):
        return len(self.usuarios)
             
class Usuario:
    def __init__(self, id, nombre, sexo, suscripcion):
        self.id =id
        self.nombre = nombre
        self.sexo = sexo
        self.suscripcion = suscripcion

    def anyadirSuscripcion(self, suscripcion):
        self.suscripcion = suscripcion
        
class Suscripcion:
     def __init__(self, id, tipo, fechaAlta, fechaFin, estado):
          self.id = id
          self.tipo = tipo
          self.fechaAlta = fechaAlta
          self.fechaFin = fechaFin
          self.estado = estado