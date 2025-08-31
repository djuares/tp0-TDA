
# Trabajo práctico 0 - Teoría de Algoritmos 2C 2025

## Alumna
 Damaris Juares - 108566

## Ejecución de pruebas
Desde la carpeta `tp0-TDA`, utilizar el siguiente comando:
```bash
 python3 src/numeros_amigos_optimizado.py --max <MAX>
```
Ejemplo:
```bash
python3 src/numeros_amigos_optimizado.py --max 100000
```

## Creación de graficos de tiempos de ejecución
Se pueden crear graficos de ejecucion de la siguiente manera:
```bash
 python3 graficos/comparacion.py 
```
El grafico se guarda en la carpeta `/graficos`

## Seguimiento de ejecuciones
Los resultados de tiempo de ejecucion correspondientes a los valores  [50000, 100000, 150000, 200000, 250000] se encuentran en `seguimiento/seguimiento_amigos_cvs.txt`.

Para realizar un nuevo seguimiento:

```bash 
 python3 seguimiento/seguimiento_con_cvs.py --max <MAX> --archivo <Archivo> 
```
