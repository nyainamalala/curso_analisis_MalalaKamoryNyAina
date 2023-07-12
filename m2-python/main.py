from fires import Fire 
from fires_database import FireDatabase

from input_read import read_int, read_float


database = FireDatabase()

while True:
    print(""" DATOS DE INCENDIO
          1 - Consulta los incendios del verano pasado (copia)
          2 - Consultar el incendio por id
          3 - Consultar el incendio por nivel
          4 - Crear y añadir un incendio por kilometro
          5 - Consultar el incendio por provincia
          6 - Guardar un incendio máximo por id
          7 - Actualizar los incendios existentes
          8 - Borrar un incendio por id
          9 - Salir de la aplicación \n
          
          """)
    
    option = int(input("Introduce una opción\n"))
    
    if option == 1:
        
        for Fire in database.find_all():
            print(Fire)
            
    elif option == 2:
        id = read_int("id")
        Fire = database.find_by_id(id)
        print(Fire)
        
    elif option == 3:
        pass
    elif option == 4:
        
        incendio_kilometro = input("Introduce el incendio por kilometro")
        incendio_nivel = read_float("Introduce el nivel de incendio")
        incendio_causa = read_int("Introduce la Causa del incendio")
        
        Incendio = Fire(None, incendio_kilometro, incendio_nivel, incendio_causa)
        
        database.save(Incendio)
        print("Los incendios añadidos correctamente")
        
        
    elif option == 5:
        pass
    
    elif option == 6:
        pass
    
    elif option == 7:
        pass
    
    else:
        print('Gracias, Ádios')
        break
    