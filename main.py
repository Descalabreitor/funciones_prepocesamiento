from preprocesado.escalar import Escalar
from preprocesado.simtonum import CodificadorEtiqueta
from preprocesado.validacion_modelo import divide_train_test
import pandas as pd
import numpy as np

prueba = ["norte","norte","sur","este","este","oeste"]
codificadorEtiqueta = CodificadorEtiqueta()
codificadorEtiqueta.ajustar(prueba)
r = codificadorEtiqueta.transformar(prueba)
print(r)
print(codificadorEtiqueta.transformar_inv(r))
pruebaescalar = [0,5,-5,2.5,-2.5]
pruebaescalar2 = [[0,10,-10,2.5,-2.5],[0,5,-5,2.5,-2.5]]
escalar = Escalar()
escalar2 = Escalar()
escalar.ajustar(pruebaescalar)
r = escalar.transformar(pruebaescalar)
escalar2.ajustar(pruebaescalar2)
t = escalar2.transformar(pruebaescalar2)
print( pruebaescalar)
print(r)
print(type(r[0]))
print(escalar.transformar_inv(r))
print("-----------------------------------")
print( pruebaescalar2)
print(t)
print(escalar2.transformar_inv(t))
pruebagrande = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
clases = ["perro", "gato", "gato", "gato", "gato", "perro", "perro", "perro", "perro" ,"perro"]
a = [4, 5, 6, 9, 8, 7, 1, 2, 3, 25]
df = pd.DataFrame()
df[1] = pruebagrande
df[2] = clases
df[3] = a
matriz_prueba = np.array([[1,2,3],[4,5,6],[7,8,9]])
resultado = divide_train_test(pruebagrande, tam_train=0.5)
print("---------------------------------------------------------------")
print(resultado)
print(type(resultado[0]))
print("---------------------------------------------------------------")
resultado = divide_train_test(pruebagrande, tam_train=5, semilla=1)
print(resultado)
print("---------------------------------------------------------------")
resultado = divide_train_test(pruebagrande, a, clases, tam_train=0.5, semilla=1)
print(resultado)
print("---------------------------------------------------------------")
resultado = divide_train_test(pruebagrande, a, clases, tam_train=5, semilla=1)
print(resultado)
print("---------------------------------------------------------------")
resultado = divide_train_test(pruebagrande, clases, tam_train=0.9, semilla=1, balancear=clases)
print(resultado)
print("---------------------------------------------------------------")
resultado = divide_train_test(pruebagrande, clases, tam_train=7, semilla=1, balancear=clases)
print(resultado)
print("---------------------------------------------------------------")
resultado = divide_train_test(df,tam_train=0.6, semilla=1)
print(resultado)
print("---------------------------------------------------------------")
resultado = divide_train_test(matriz_prueba,tam_train=0.6, semilla=1)
print(resultado)
