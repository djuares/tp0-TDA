import time
import argparse
import csv

def amigos_optimizado(MAX, archivo_csv):
    t1 = time.time()
    
    sumas_divisores = [0] * (MAX + 1)
    for numero in range(1, MAX + 1):
        for multiplo in range(numero * 2, MAX + 1, numero):
            sumas_divisores[multiplo] += numero
    
    amigos = []
    for numero1 in range(1, MAX + 1):
        numero2 = sumas_divisores[numero1]
        if numero2 <= MAX and numero2 != numero1:
            if numero2 > numero1 and sumas_divisores[numero2] == numero1:
                amigos.append((numero1, numero2))
    
    t2 = time.time()
    tiempo = t2 - t1
    
    # Guardar en CSV (modo append para no borrar resultados previos)
    # Escribimos cabecera solo si el archivo está vacío o no existe
    try:
        with open(archivo_csv, 'r', newline='') as f:
            primera_linea = f.readline()
    except FileNotFoundError:
        primera_linea = ''
    
    with open(archivo_csv, 'a', newline='') as f:
        escritor = csv.writer(f)
        if not primera_linea:
            escritor.writerow(['Max', 'Tiempo (s)', 'Cantidad Pares', 'Numero1', 'Numero2'])
        for a, b in amigos:
            escritor.writerow([MAX, f"{tiempo:.4f}", len(amigos), a, b])
    
    print(f"MAX={MAX} - Tiempo: {tiempo:.4f} seg - Pares encontrados: {len(amigos)}")
    print(f"Resultados guardados en '{archivo_csv}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Buscar números amigos hasta un valor máximo.")
    parser.add_argument('--max', type=int, required=True, help='Valor máximo para buscar números amigos')
    parser.add_argument('--archivo', type=str, default='resultados_amigos.csv', help='Archivo CSV donde guardar resultados')
    args = parser.parse_args()
    
    amigos_optimizado(args.max, args.archivo)
