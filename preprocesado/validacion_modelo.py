import pandas as pd
import numpy as np


def divide_train_test(*datos, tam_train, semilla=None, mezclar=True, balancear=None):
    final = []
    if semilla is not None:
        np.random.seed(semilla);
    tamaño = len(datos[0])

    if mezclar is False and balancear is not None:
        raise ValueError("Mezclar must be true to use balancear")

    if tam_train < 0:
        raise ValueError("tam_train must be a positive value")

    if tam_train > len(datos[0]):
        raise ValueError("tam_train must be smaller or equal to the length of the values")


    if mezclar and balancear is not None:
        clases = datos[1]
        valores = datos[0]

        if len(clases) != len(valores):
            raise ValueError("Values and Clases must be the same size!")

        proporciones = {}
        final = [[], []]

        valores = np.array(valores)
        for index in range(len(clases)):
            if clases[index] in proporciones.keys():
                proporciones[clases[index]][0] += 1 / len(valores)
                proporciones[clases[index]].append(valores[index])
            if clases[index] not in proporciones.keys():
                proporciones[clases[index]] = [1 / len(valores)]
                proporciones[clases[index]].append(valores[index])

        if tam_train < 1:
            for clase in proporciones.keys():
                i = int((len(valores) * tam_train * proporciones[clase][0]))
                final[0].extend(proporciones[clase][1:i+1])
                final[1].extend(proporciones[clase][i+1:])

        if tam_train > 1:
            for clase in proporciones.keys():
                i = int((tam_train * proporciones[clase][0]))
                final[0].extend(proporciones[clase][1:i+1])
                final[1].extend(proporciones[clase][i+1:])

    else:
        for estructura in datos:
            if len(estructura) != tamaño:
                raise Exception("All data structures must be the same size")
            if mezclar:
                estructura = barajar(estructura)
            if tam_train > 1:
                final.append(estructura[:tam_train])
                final.append(estructura[tam_train:])
            if 0 < tam_train < 1:
                i = int(len(estructura) * tam_train)
                final.append(estructura[:i])
                final.append(estructura[i:])
    return final

def to_original(lista, tipo_org):
    if tipo_org == 0:
        lista = pd.DataFrame(lista)
    elif tipo_org == 1:
        lista = np.array(lista)
    else:
        lista = lista
    return lista

def barajar(datos):
    if type(datos) is pd.DataFrame:
        datos_shuffled = datos.iloc[np.random.permutation(datos.index)].reset_index(drop=True)
    else:
        datos_shuffled = np.random.permutation(datos)
    return datos_shuffled