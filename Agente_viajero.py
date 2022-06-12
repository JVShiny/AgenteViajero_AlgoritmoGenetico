from Funciones import *
import pandas as pd
import numpy as np
import random

### PARAMTROS INICIALES DEL ALGORITMO
prob_cruzamiento = 0.85
prob_mutacion = 0.1

### IMPORTACION DE DATOS
ciudades = pd.read_csv('Ciudades.csv', header=0)
ciudades_df = pd.DataFrame(ciudades, columns=['X','Y'])
rows, columns = ciudades_df.shape
matriz_dist = np.zeros((rows,rows))
# print(ciudades_df)
# print(rows,columns)

### CALCULANDO MATRIZ DE DISTANCIAS
for i in range(rows):
    for j in range(rows):
        matriz_dist[i][j] = dist(ciudades_df.iloc[j,0], ciudades_df.iloc[i,0], ciudades_df.iloc[j,1], ciudades_df.iloc[i,1])
matriz_dist = pd.DataFrame(matriz_dist)
print("MATRIZ DE DISTANCIAS")
print(matriz_dist)

# x = [1,4,3,2,5]
# distancia_total = fitnes(x,matriz_dist)
# print(x)
# print(distancia_total)
### INICIO DE AG
tamaño_poblacion = 10
generaciones = 10
if tamaño_poblacion%2 != 0:
    iteraciones_generacion = int((tamaño_poblacion+1)/2)
    añadir = True
else:
    iteraciones_generacion = int(tamaño_poblacion/2)
#tamaño_poblacion = int(input("Ingrese el tamaño de la poblacion: "))   #Cambio a hacer por el usuario
sec_ciudades = sec(rows)  #Parametro para generar numeros aleatorios para muestras
sec_poblacion = sec(tamaño_poblacion)  #Parametro para generar numeros aleatorios para torneo
fitnes_poblacion = []
poblacion = np.zeros((tamaño_poblacion,rows),int)
poblacion = pd.DataFrame(poblacion)
for i in range(tamaño_poblacion):
    poblacion.iloc[i,:] = random.sample(sec_ciudades,rows)
    fitnes_poblacion.append(fitnes(poblacion.iloc[i,:], matriz_dist))
print("POBLACION GENERACIÓN 0")
print(poblacion)
print("FITNES POBLACION")
print(fitnes_poblacion)
print("COSTO TOTAL POBLACION")
costo_total = costo_total_poblacion(fitnes_poblacion)
print(costo_total)

for gen in range(1,generaciones):
    nueva_gen = []
    for it in range(iteraciones_generacion):
        # SELECCIÓN
        #La selección se hara por torneo
        numero_competidores = 3
        while True:
            index_ganador1, ganador1 = seleccion_torneo(sec_poblacion, numero_competidores, fitnes_poblacion)
            index_ganador2, ganador2 = seleccion_torneo(sec_poblacion, numero_competidores, fitnes_poblacion)
            #Guardando padres 
            padre1 = []
            padre2 = []
            for i in range(rows):
                padre1.append(poblacion.iloc[index_ganador1,i])
                padre2.append(poblacion.iloc[index_ganador2,i])
            if index_ganador1 != index_ganador2:
                break
        print("SELECCION DE TORNEO")
        print(index_ganador1, index_ganador2)
        print(ganador1, ganador2)
        print(padre1)
        print(padre2)

        numero_random1 = random.random()
        if numero_random1 < prob_cruzamiento:
            ## CRUZAMIENTO
            #El cruzamiento se hara por 2 puntos
            hijo1 = cruzamiento(padre1, padre2)
            hijo2 = cruzamiento(padre1, padre2)
            print("HIJOS")
            print(hijo1)
            print(hijo2)
        else:
            hijo1 = padre1.copy()
            hijo2 = padre2.copy()
            print("HIJOS")
            print(hijo1)
            print(hijo2)

        ## FUNCIÓN DE MUTACIÓN
        #La mutación se hará por intercambio de 2 posiciones
        numero_random2 = random.random()
        numero_random3 = random.random()
        if numero_random2 < 0.5:
            if numero_random3 < prob_mutacion:
                hijo1 = mutacion(hijo1,rows)
        else:
            if numero_random3 < prob_mutacion:
                hijo2 = mutacion(hijo2,rows)
            print("MUTACION")
            print(hijo1)
            print(hijo2)
        ## REEMPLAZO POBLACIÓN
        fitnes_padre1 = fitnes(padre1, matriz_dist)
        fitnes_padre2 = fitnes(padre2, matriz_dist)
        fitnes_hijo1 = fitnes(hijo1, matriz_dist)
        fitnes_hijo2 = fitnes(hijo2, matriz_dist)
        if fitnes_hijo1 <= fitnes_padre1:
            nueva_gen.append(hijo1)
        else:
            nueva_gen.append(padre1)
        if fitnes_hijo2 <= fitnes_padre2:
            nueva_gen.append(hijo2)
        else:
            nueva_gen.append(padre2)
    nueva_gen = pd.DataFrame(nueva_gen)
    print("GENERACION" + str(gen+1))
    print(nueva_gen)
    poblacion = nueva_gen.copy()

    nueva_fitnes_poblacion = []
    for i in range(tamaño_poblacion):
        nueva_fitnes_poblacion.append(fitnes(poblacion.iloc[i,:], matriz_dist))
    fitnes_poblacion = []
    fitnes_poblacion = nueva_fitnes_poblacion.copy()
    print("COSTO TOTAL POBLACION")
    costo_total = costo_total_poblacion(fitnes_poblacion)
    print(costo_total)

    
        

    






















