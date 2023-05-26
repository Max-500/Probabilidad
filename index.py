import numpy as np
import math

# Ingresamos los datos
datos = [782, 1333, 515, 1475, 696, 832, 1052, 700, 987, 542,
1296, 704, 814, 1482, 1023, 739, 643, 956, 1023, 784,]

# Ordenamos los datos
datos.sort()

# Cálculamos la amplitud
K = 1 +(10/3) * np.log10(len(datos))

# Redondemos el valos
K = int(K.round(0))

# Cálculamos el rango
R = max(datos) - min(datos)

# Cálculamos la amplitud
A = R / K
A = math.ceil(A)

data = {
'Clase' : [],
'Limite Inferior': [],
'Limite Superior': [],
'Frecuencia': [],
'Marca de Clase': [],
'Limite Inferior Exacto': [],
'Limite Superior Exacto': []
}

# Inicializar variables
hay_decimal = False
contador_decimales = 0
max_decimales = 0

# Recorre la lista de números
for n in datos:
if isinstance(n, float):
hay_decimal = True
decimales = len(str(n).split('.')[1])
if decimales > max_decimales:
max_decimales = decimales
numero_con_mas_decimales = n

if hay_decimal :
uv = max_decimales
else:
uv = 1

# Dividimos los datos en K clases y asignamos una letra a cada clase
letras = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

for i in range(K):
    data['Clase'].append(letras[i])

limite_inferior = min(datos)
limite_superior = 0

while max(datos) > limite_superior:
    data['Limite Inferior'].append(limite_inferior)
    limite_superior = limite_inferior + A - uv
    data['Limite Superior'].append(limite_superior)
    limite_inferior =limite_superior + uv

for n in range(K):
    inferior = data['Limite Inferior'][n]
    superior = data['Limite Superior'][n]
    frecuencia = 0
    for i in datos:
        if inferior <= i <= superior:
            frecuencia += 1
            

print(data)