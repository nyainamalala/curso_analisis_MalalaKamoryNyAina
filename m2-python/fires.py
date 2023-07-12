# CLASE FIRE

class Fire:
    def __init__ (self, id, provincia, nivel, causa):
        self.id = id
        self.provincia = provincia
        self.nivel = nivel
        self.causa = causa
        
    def __str__(self):
        return f"Incendio {self.id}: en {self.provincia}, kilómetro {self.kilometro}. Nivel: {self.nivel}. Causa: {self.causa}"


# Importar la clase Fire desde el archivo python.py 

from fires import Fire

incendio = Fire(100, 'Madrid', 'Alto', 'Desconocido')
incendio1 = Fire(200, 'Tana', 'Medio', 'Incendio forestal')
incendio2 = Fire(300, 'Granada', 'Alto', 'Fuego voluntario')

print('El incendio en Madrid el verano pasado')
print(incendio.provincia)
print(incendio.nivel)
print(incendio.causa)


print('El incendio en Tana el verano pasado')
print(incendio1.provincia)
print(incendio1.nivel)
print(incendio1.causa)

print('El incendio en Granada el verano pasado')
print(incendio2.provincia)
print(incendio2.nivel)
print(incendio2.causa)
