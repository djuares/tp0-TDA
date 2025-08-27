import time
import math
import matplotlib.pyplot as plt

import time

def amigos_optimizado_solo_tiempo(MAX):
    t1 = time.time()
    
    sumas_divisores = [0] * (MAX + 1)
    for numero in range(1, MAX + 1):
        for multiplo in range(numero * 2, MAX + 1, numero):
            sumas_divisores[multiplo] += numero
    
    for numero1 in range(1, MAX + 1):
        numero2 = sumas_divisores[numero1]
        if numero2 <= MAX and numero2 != numero1 and sumas_divisores[numero2] == numero1:
            pass  
    
    t2 = time.time()
    return t2 - t1


def amigos_no_optimizado(MAX):
    t1 = time.time()
    numeros_amigos = set()
    
    for i in range(1, MAX + 1):
        s = 0
        for j in range(1, i):
            if i % j == 0:
                s += j
        s2 = 0
        for k in range(1, s):
            if s % k == 0:
                s2 += k
        if i == s2 and i != s:
            amigos = tuple(sorted([i, s]))
            numeros_amigos.add(amigos)
    
    t2 = time.time()
    return t2 - t1, numeros_amigos

def medir_tiempos(lista_tamanios):
    tiempos = []
    for n in lista_tamanios:
        print(f"Ejecutando para N = {n}")
        tiempo = amigos_optimizado_solo_tiempo(n)
        print(f"Tiempo: {tiempo:.4f} segundos")
        tiempos.append(tiempo)
    return tiempos



import matplotlib.pyplot as plt

def graficar_tiempos(tamanios, tiempos):
    plt.figure(figsize=(10,6))
    plt.plot(tamanios, tiempos, 'o-', color='blue', label='Algoritmo Optimizado - Solo Tiempo')
    plt.xlabel('Tamaño máximo (N)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Tiempos de ejecución - Algoritmo Optimizado')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True, which="both", ls="--", alpha=0.5)
    
    for x, y in zip(tamanios, tiempos):
        plt.annotate(f"{y:.2f}s", (x, y), textcoords="offset points", xytext=(0,5), ha='center')
    
    plt.legend()
    plt.tight_layout()
    plt.savefig('graficos/tiempos_amigos_optimizado.png', dpi=300)
    plt.show()
    print("Gráfico guardado como 'tiempos_amigos_optimizado.png'")

if __name__ == "__main__":
    tamanios = [50000, 100000, 150000, 200000, 250000]
    tiempos = medir_tiempos(tamanios)
    graficar_tiempos(tamanios, tiempos)
