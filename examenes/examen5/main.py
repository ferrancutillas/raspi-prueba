from modelos import Gimnasio, Usuario, Suscripcion

g1 = Gimnasio(101, "BasicFit", 200)
g2 = Gimnasio(102, "SynerGym", 175)

s1 = Suscripcion(301, "Premium", "21/04/2026", "21/05/2026", True)
s2 = Suscripcion(301, "Básica", "22/02/2026", "22/03/2026", False)

u1 = Usuario(201, "Ferran Cutillas", "M", s1)
u2 = Usuario(202, "Marta Moreno", "F", s2)
u3 = Usuario(203, "Victor Romero", "M", s1)

g1.anyadirUsuario(u1)
g1.anyadirUsuario(u2)

for usuario in g1.consultarUsuarios():
    if usuario.suscripcion.estado:
        print(f"La suscripción de {usuario.nombre} está activa")
    else:
        print(f"La suscripción de {usuario.nombre} está inactiva")
