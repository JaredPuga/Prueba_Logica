def Recorrer(filas, columnas):
    matriz = [[None for j in range(columnas)] for i in range(filas)]
    limite_superior = 0
    limite_inferior = filas - 1
    limite_izquierdo = 0
    limite_derecho = columnas - 1
    
    valores = []
    elementos_recorridos = []

    while limite_superior <= limite_inferior and limite_izquierdo <= limite_derecho:
        
        #DERECHA
        for i in range(limite_izquierdo, limite_derecho + 1):
            elementos_recorridos.append(matriz[limite_superior][i])
            valores.append('R')
        limite_superior += 1
        
        #ABAJO
        for i in range(limite_superior, limite_inferior + 1):
            elementos_recorridos.append(matriz[i][limite_derecho])
            valores.append('D')
        limite_derecho -= 1
        
        # IZQUIERDA
        if limite_superior <= limite_inferior:
            for i in range(limite_derecho, limite_izquierdo - 1, -1):
                elementos_recorridos.append(matriz[limite_inferior][i])
                valores.append('L')
            limite_inferior -= 1
        
        # ARRIBA
        if limite_izquierdo <= limite_derecho:
            for i in range(limite_inferior, limite_superior - 1, -1):
                elementos_recorridos.append(matriz[i][limite_izquierdo])
                valores.append('U')
            limite_izquierdo += 1
    
    return valores


T = int(input())

direccion_final = []

for i in range(T):
    N, M = map(int, input().split())
    elementos_recorridos = Recorrer(N, M)
    direccion_final.append(elementos_recorridos.pop(-1)) #pop -1 me retorna el último elemento de la lista

for i in range(T):
    print(direccion_final[i])