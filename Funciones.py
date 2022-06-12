import math
import pandas as pd
import random

##Funcion para crear una lista del numero de ciudades
def sec(n_ciudades):
    secuencia = []
    for i in range(1,n_ciudades+1):
        secuencia.append(i)
    return secuencia

## Funcion para obtener la distancia entre dos puntos
def dist(x2,x1,y2,y1):
    distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distancia

## Funcion para obtener el fitnes 
def fitnes(vector, matriz_distancias):
    total = 0
    n = len(vector)
    #matriz_distancias = pd.DataFrame(matriz_distancias)
    for i in range(n-1):
        total = total + matriz_distancias.iloc[vector[i]-1,vector[i+1]-1]
    distancia_total = total + matriz_distancias.iloc[vector[n-1]-1,0]
    return distancia_total

## Funcion para encontrar minimo entre los competidores
def minimo_competidores(competidores):
    menor = competidores[0]
    for i in competidores:
        if i < menor:
            menor = i
    return menor
## Funcion de seleccion de padres
def seleccion_torneo(secuencia_poblacion, num_competidores, fitnes_list):
    competidores_index = random.sample(secuencia_poblacion, num_competidores)
    competidores_valor = []
    for i in competidores_index:
        competidores_valor.append(fitnes_list[i-1])
    winner = minimo_competidores(competidores_valor)
    winner_index = fitnes_list.index(winner)
    return winner_index, winner

## Funcion de cruzamiento
def cruzamiento(padre1, padre2):
    n = len(padre1)
    n_sec = sec(n)
    primer_corte = random.randint(0, n-1)
    pos_prohibidas = [abs(primer_corte-2), abs(primer_corte-1), primer_corte, abs(primer_corte+1), abs(primer_corte+1)]
    valores_para_segundo_corte = list(set(n_sec)-set(pos_prohibidas))
    segundo_corte = random.sample(valores_para_segundo_corte, 1)
    segundo_corte_int = int(segundo_corte[0])
    punto_corte1= min(primer_corte, segundo_corte_int)
    punto_corte2 = max(primer_corte, segundo_corte_int)
    primer_bloque = (padre1[0:punto_corte1] + padre1[punto_corte2:n-1])
    rellenar_corte = list(set(padre2) - set(primer_bloque))
    hijo = (padre1[0:punto_corte1] + rellenar_corte + padre1[punto_corte2:n-1])
    return hijo


## Función de mutación
def mutacion(hijo, len_hijo):
    sec_n = sec(len_hijo)
    puntos_a_intercambiar = random.sample(sec_n, 2)
    punto1 = min(puntos_a_intercambiar)-1
    punto2 = max(puntos_a_intercambiar)-1
    valor_aux = hijo[punto1]
    hijo[punto1] = hijo[punto2]
    hijo[punto2] = valor_aux
    return hijo

## Costo total de la poblacion
def costo_total_poblacion(vector):
    costo_total = 0
    for i in vector:
        costo_total = costo_total + i
    return costo_total







