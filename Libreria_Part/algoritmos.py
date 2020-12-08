# algortimos.py
import math

def distancia_euclidiana(origen_x, origen_y, destino_x, destino_y):
   return math.sqrt((destino_x - origen_x)**2 + (destino_y - origen_y)**2)