import numpy as np
import pandas as pd


class Escalar:
    def __init__(self):
        self.min = 0
        self.max = 0

    def ajustar(self, x, Min=-1, Max=1):
        if type(x[0]) is float or type(x[0]) is int:
            self.tipo_org = get_tipo_org(x)
            self.max = Max
            self.Xmax = np.max(x)
            self.Xmin = np.min(x)
            self.constant = ((Min * self.Xmax) - (Max * self.Xmin)) / (self.Xmax - self.Xmin)
            self.constant_inv = ((self.Xmin * Max) - (Min * self.Xmax)) / (Max - Min)
        else:
            self.tipo_org = []
            self.Xmin = []
            self.Xmax = []
            self.constant = []
            self.constant_inv = []
            for estructura in x:
                self.tipo_org.append(get_tipo_org(estructura))
                self.Xmin.append(np.min(estructura))
                self.Xmax.append(np.max(estructura))
                self.constant.append(((Min * np.max(estructura)) - (Max * np.min(estructura))) / (np.max(estructura) - np.min(estructura)))
                self.constant_inv.append(((np.min(estructura) * Max) - (Min * np.max(estructura))) / (
                            Max - Min))

    def transformar(self, x):
        x = np.array(x, dtype="float64")
        resultado = []

        for i in range(len(x)):
            value = x[i]
            if type(value) == np.float64:
                resultado.append((((self.max - self.min) * value) / (self.Xmax - self.Xmin)) + self.constant)
                resultado = to_original(resultado,self.tipo_org)
            else:
                resultado.append(to_original(
                    [(((self.max - self.min) * number) / (self.Xmax[i] - self.Xmin[i])) + self.constant[i] for number in
                     value],self.tipo_org[i]))

        return resultado

    def transformar_inv(self, x):
        x = np.array(x, dtype="float64")
        resultado = []

        for i in range(len(x)):
            value = x[i]
            if type(value) == np.float64:
                resultado.append((((self.Xmax - self.Xmin) * value) / (self.max - self.min)) + self.constant_inv)
                resultado = to_original(resultado, self.tipo_org)
            else:
                resultado.append(to_original(
                    [(((self.Xmax[i] - self.Xmin[i]) * number) / (self.max - self.min)) + self.constant_inv[i] for
                     number in value], self.tipo_org[i]))

        return resultado


def to_original(lista, tipo_org):
    if tipo_org == 0:
        lista = pd.DataFrame(lista)
    elif tipo_org == 1:
        lista = np.array(lista)
    else:
        lista = lista
    return lista


def get_tipo_org(x):
    if isinstance(x, pd.DataFrame):
        num = 0
    elif isinstance(x, np.ndarray):
        num = 1
    elif isinstance(x, list):
        num = 2
    else:
        raise TypeError("Entry data must be an array, npArray or list")
    return num
