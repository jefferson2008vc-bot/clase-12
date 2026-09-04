print("MATRIZ DE ASIENTOS 3×4")

print("Estado de los asientos: 0 = Disponible, 1 = Reservado")
filas = 3
columnas = 4
asientos = [[0 for _ in range(columnas)] for _ in range(filas)]

print("Se identifica con letras las filas")
letras_filas = ['A', 'B', 'C']

print()
def mostrar_asientos():
    """Muestra el mapa de la sala con leyenda"""
    print("\n" + "="*30)
    print("MAPA DE LA SALA")
    print("="*30)
    print("   1️⃣  2️⃣  3️⃣  4️⃣")
    print("   ─────────────────────")
    
    for i in range(filas):
        print(f"{letras_filas[i]} ", end="│")
        for j in range(columnas):
            if asientos[i][j] == 0:
                print(" 🟩 ", end="") 
            else:
                print(" 🟥 ", end="") 
        print("│")
    
    print("   ─────────────────────")
    print("🟩 = Disponible   🟥 = Reservado")
    print("="*30 + "\n")

print("Reserar asientos")
def reservar_asiento(fila, columna):
    """mensaje de estado de asientos"""
    fila = fila.upper().strip()
    if fila not in letras_filas:
        return "Inválido, seleccione A, B o C."
    
    indice_fila = letras_filas.index(fila)
    
    if not (1 <= columna <= 4):
        return "Inválido, seleccione del 1 al 4."
    
    indice_columna = columna - 1
    
    if asientos[indice_fila][indice_columna] == 1:
        return f"El asiento {fila}{columna} ya está reservado."
    
    asientos[indice_fila][indice_columna] = 1
    return f"¡As reservaso con exito! El asiento {fila}{columna} reservado."

print("MOSTRAR ASIENTOS DISPONIBLES")

def mostrar_disponibles():
  print("Vista de los asientos libres")
  print("\n Asientos disponibles:")
  disponibles = []
  for i in range(filas):
        for j in range(columnas):
            if asientos[i][j] == 0:
                disponibles.append(f"{letras_filas[i]}{j+1}")
    
        if disponibles:
         print("  • " + ", ".join(disponibles))
        else:
         print("No hay asientos disponibles. ¡Sala completa!")
        print()


def menu_principal():
    print("Opciones del sistema")
    while True:
        print("\n" + ""*35)
        print(" SISTEMA DE RESERVA DE CINE")
        print(""*35)
        print("1️ - Ver mapa de asientos")
        print("2️ - Reservar un asiento")
        print("3️ - Ver asientos disponibles")
        print("4️ - Salir del sistema")
        print(""*35)
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            mostrar_asientos()
        
        elif opcion == "2":
            print("\n Realizar Reserva")
            fila = input("Ingresa la fila (A, B o C): ")
            try:
                columna = int(input("Ingresa el número de asiento (1-4): "))
                mensaje = reservar_asiento(fila, columna)
                print(mensaje)
            except ValueError:
                print("Invalido,selecciona un número para la columna.")
        
        elif opcion == "3":
            mostrar_disponibles()
        
        elif opcion == "4":
            print("\n Gracias por confiar en nosotros. ¡Vuelve pronto!")
            break
        
        else:
            print(" Lo sentimos. Intenta nuevamente.")
print()

                                                                                                                        

print()
if __name__ == "__main__":
    print("\n Bienvenido al mejor lugar de reservas")
    menu_principal()