def main():
    """
    Programa que lea como entrada la posición origen y la posición destino de un caballo y \n
    de como salida un mensaje de si el movimiento es válido o no para el caballo.
    Entradas y restricciones:
    - Fila, Columna : Posición del caballo y del destino, entero de 0 a 8.
    Salidas:
    Mensaje que dice si el movimiento del caballo es válido o no.
    """
    
    print("Movimientos válidos de un caballo de ajedrez. ")
    
#Solicitud valores
    
    print("Escriba la posición actual de la figura: ")
    filaC = int(input("Fila (1-8): "))
    if filaC not in [1,2,3,4,5,6,7,8]:
        print("Fila no válida, el valor debe estar entre 1 y 8.")
        input()
        return
    columnaC = int(input("Columna (1-8): "))
    if columnaC not in [1,2,3,4,5,6,7,8]:
        print("Columna no válida, el valor debe estar entre 1 y 8.")
        input()
        return

    print("Escriba la posición destino de la figura: ")
    filaD = int(input("Fila (1-8): "))
    if filaD not in [1,2,3,4,5,6,7,8]:
        print("Fila no válida, el valor debe estar entre 1 y 8.")
        input()
        return
    columnaD = int(input("Columna (1-8): "))
    if columnaD not in [1,2,3,4,5,6,7,8]:
        print ("Columna no válida, el valor debe estar entre 1 y 8.")
        input()
        return

#Cálculo posiciones:

    if (filaC in [1,2,3,4,5,6,7,8] and columnaC in [1,2,3,4,5,6,7,8]) and (filaD == filaC + 1 and columnaD == columnaC +2):
        print("El movimiento es válido. ")
    elif (filaC in [1,2,3,4,5,6,7,8] and columnaC in [1,2,3,4,5,6,7,8]) and (filaD == filaC + 2 and columnaD == columnaC + 1):
        print("El movimiento es válido. ")
    elif (filaC in [1,2,3,4,5,6,7,8] and columnaC in [1,2,3,4,5,6,7,8]) and (filaD == filaC + 2 and columnaD == columnaC - 1):
        print("El movimiento es válido. ")
    elif (filaC in [1,2,3,4,5,6,7,8] and columnaC in [1,2,3,4,5,6,7,8]) and (filaD == filaC + 1 and columnaD == columnaC - 2):
        print("El movimiento es válido. ")
    elif (filaC in [1,2,3,4,5,6,7,8] and columnaC in [1,2,3,4,5,6,7,8]) and (filaD == filaC - 1 and columnaD == columnaC - 2):
        print("El movimiento es válido. ")
    elif (filaC in [1,2,3,4,5,6,7,8] and columnaC in [1,2,3,4,5,6,7,8]) and (filaD == filaC - 2 and columnaD == columnaC - 1):
        print("El movimiento es válido. ")
    elif (filaC in [1,2,3,4,5,6,7,8] and columnaC in [1,2,3,4,5,6,7,8]) and (filaD == filaC - 2 and columnaD == columnaC + 1):
        print("El movimiento es válido. ")
    elif (filaC in [1,2,3,4,5,6,7,8] and columnaC in [1,2,3,4,5,6,7,8]) and (filaD == filaC - 1 and columnaD == columnaC + 2):
        print("El movimiento es válido. ")
    else:
        print("El movimiento no es válido. ")
    input()
main()
