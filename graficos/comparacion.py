import time
import math
import matplotlib.pyplot as plt

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

    for numero1 in range(MAX + 1):
        numero2 = sumas_divisores[numero1]
        
        # Verificar condiciones para números amigos
        if numero2 <= MAX and sumas_divisores[numero2] == numero1:
            amigos = tuple(sorted([numero1, numero2]))
            if amigos not in numeros_amigos:
                numeros_amigos.add(amigos)
            
    
    t2 = time.time()
    return t2 - t1, numeros_amigos

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

def generar_mediciones():
    # Solo los tamaños grandes pedidos
    tamanios = [50000, 100000, 150000, 200000, 250000]
    tiempos_optimizado = []

    for tamanio in tamanios:
        print(f"\nProbando con tamaño: {tamanio}")

        # Medir solo el optimizado
        tiempo_opt, amigos_opt = amigos_optimizado(tamanio)
        tiempos_optimizado.append(tiempo_opt)

        print(f"  Optimizado: {len(amigos_opt)} pares, {tiempo_opt:.4f} segundos")

    return tamanios, tiempos_optimizado


def generar_grafico(tamanios, tiempos_optimizado):
    plt.figure(figsize=(12, 8))

    # Graficar solo el algoritmo optimizado
    plt.plot(tamanios, tiempos_optimizado, 'o-', linewidth=2, markersize=8,
             label='Algoritmo Optimizado', color='blue')

    plt.xlabel('Tamaño máximo (N)', fontsize=12)
    plt.ylabel('Tiempo de ejecución (segundos)', fontsize=12)
    plt.title('Tiempos de Ejecución: Algoritmo Optimizado de Números Amigos', fontsize=14)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')

    # Anotar valores exactos en el gráfico
    for i, t in enumerate(tiempos_optimizado):
        plt.annotate(f'{t:.2f}s', (tamanios[i], t), textcoords="offset points", xytext=(0, 10), ha='center')

    plt.tight_layout()
    plt.savefig('ComparacionOptimizado.png', dpi=300)
    print("✅ Gráfico guardado como 'ComparacionOptimizado.png'")
    plt.show()


if __name__ == "__main__":
    tamanios, tiempos_optimizado = generar_mediciones()
    generar_grafico(tamanios, tiempos_optimizado)
