# CLASE FIRE

class Fire:
    def __init__ (self, provincia, kilometro, nivel, causa):
        self.id = None
        self.provincia = provincia
        self.kilometro = kilometro
        self.nivel = nivel
        self.causa = causa
        
    def __str__(self):
        return f"Incendio {self.id}: en {self.provincia}, kilómetro {self.kilometro}. Nivel: {self.nivel}. Causa: {self.causa}"


# Importar la clase Fire desde el archivo python.py 

from fires import Fire

incendio = Fire('Madrid', 20, 'Alto', 'Desconocido')
incendio1 = Fire('Tana', 15, 'Medio', 'Incendio forestal')
incendio2 = Fire('Granada', 40, 'Alto', 'Fuego voluntario')

print('EL incendio en Madrid este pasado')
print(incendio.provincia)
print(incendio.kilometro)
print(incendio.nivel)
print(incendio.causa)


print('EL incendio en Tana este pasado')
print(incendio1.provincia)
print(incendio1.kilometro)
print(incendio1.nivel)
print(incendio1.causa)

print('EL incendio en Granada este pasado')
print(incendio2.provincia)
print(incendio2.kilometro)
print(incendio2.nivel)
print(incendio2.causa)


# CLASE FIREDATABASE

from fires import Fire

class FireDatabase:
    def __init__(self):
        self.fires = []
        
    def find_all(self):
        return self.fires.copy()
    
    def find_by_id(self, fire_id):
        for fire in self.fires:
            if fire.id == fire_id:
                return fire
        return None
    def find_by_level(self, level):
        result = []
        for fire in self.fires:
            if fire.nivel == level:
                result.