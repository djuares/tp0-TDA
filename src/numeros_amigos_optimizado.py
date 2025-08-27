import time
import math

def amigos_optimizado(MAX):
    t1 = time.time()
    
    # Registrar sumas de divisores
    sumas_divisores = [0] * (MAX + 1)
    
    # Buscar divisores a partir de los multiplos
    for numero in range(1, MAX + 1):
        for multiplo in range(numero * 2, MAX + 1, numero):
            sumas_divisores[multiplo] += numero
    
    # Buscar pares de números amigos
    numeros_amigos = set()

    for numero1 in range(MAX) :
        numero2 = sumas_divisores[numero1]
        
        # Verificar condiciones para números amigos
        if numero2 <= MAX and sumas_divisores[numero2] == numero1:
            amigos = tuple(sorted([numero1, numero2]))
            if amigos not in numeros_amigos:
                print(numero1,numero2)
                numeros_amigos.add(amigos)
            
    
    t2 = time.time()
    print(t2-t1)

amigos_optimizado(100000)