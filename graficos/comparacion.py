import time
import math
import matplotlib.pyplot as plt

import time

def amigos_optimizado_solo_tiempo(MAX):
    t1 = time.time()
    
    sumas_divisores = [0] * (MAX + 1)
    for numero in range(1, MAX):
        for multiplo in range(numero * 2, MAX+1, numero):
            sumas_divisores[multiplo] += numero
    
    for numero1 in range(MAX+1):
        numero2 = sumas_divisores[numero1]
        if numero2 <= numero1 and sumas_divisores[numero2] == numero1:
            print(numero1, numero2)  
    
    t2 = time.time()
    return t2 - t1

def medir_tiempos(lista_tamanios):
    tiempos = []
    for n in lista_tamanios:
        print(f"Ejecutando para N = {n}")
        tiempo = amigos_optimizado_solo_tiempo(n)
        print(f"Tiempo: {tiempo:.4f} segundos")
        tiempos.append(tiempo)
    return tiempos


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
