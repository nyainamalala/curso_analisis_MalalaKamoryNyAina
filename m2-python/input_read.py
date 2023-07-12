
def read_int(incendio):
    while True:
        try:
            result = int(input(f"Introduce datos de incendio {incendio}"))
            return result
        except ValueError:
            print("Los valores añadisios son erróneos")
            
def read_float(incendio):
    while True:
        try:
            result = float(input(f"Introduce datos de incendio {incendio}"))
            return round(result, 2)
        except ValueError:
            print("Los valores añadidos son erróneos")


