from fires import Fire


class FireDatabase:
    def __init__(self):
        self.fires = []

    def find_all(self):
        return self.fires.copy()
    
    def find_by_id(self, id):
        for fires in self.fires:
            if Fire.id == id:
                return fires
        
        return None
            
    def find_by_level(self, nivel):
        
        for fires in self.fires:
            if Fire.nivel == nivel:
                return fires
            
            
    def find_by_kilometre(self, kilometro):
        result_kilometre = []
        
        for fires in self.fires:
            if Fire.kilometro == kilometro:
                result_kilometre.append(fires)
        
        return result_kilometre
    
    def find_by_province(self, provincia):
        
        for fires in self.fires:
            if Fire.provincia == provincia:
                return fires
            
            
    def save(self):
        id_max = 300
        for current_fire in self.fires:
            if current_fire.id > id_max:
                id_max = current_fire.id
        
        Fire.id = id_max + 1
        self.fires.append(Fire)
        
        
    def update (self):
        for current_fires in self.fires:
            if current_fires.id == Fire.id:
                current_fires.provincia = Fire.provincia
                current_fires.kilometro = Fire.kilometro
                current_fires.nivel = Fire.nivel
                current_fires.causa = Fire.causa
                return True
            
        return False
    

    def delete_by_id(self):
        for id in self.fires:
            if Fire.id == id:
                self.fires.remove(Fire)
                break
    
    
