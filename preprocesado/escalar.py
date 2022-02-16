import numpy as np

class Escalar:
    def __init__(self):
        self.min = 0
        self.max = 0
        self.xmax = 0
        self.xmin = 0
        self.constant = 0
        self.constant_inv = 0
        self.ajustes = []

    def ajustar(self, x, Min=-1, Max=1):
        self.min = Min
        self.max = Max
        for index in range(len(x)):
            if type(x[index]) is int or type(x[index]) is float:
                self.xmin = np.min(x)
                self.xmax = np.max(x)
                self.constant = (self.min*self.xmax - self.max * self.xmin) / (self.xmax - self.xmin)
                self.constant_inv = (self.xmin * self.max - self.xmax *self.min) / (self.max - self.min)
                return None
            else:
                escalar = Escalar()
                escalar.ajustar(x[index], Min, Max)
                self.ajustes.append(escalar)

    def transformar(self, x):
        resultado = []
        for index in range(len(x)):
            if type(x[index]) is int or type(x[index]) is float:
                resultado.append((((self.max - self.min) * x[index]) / (self.xmax - self.xmin)) + self.constant)
            else:
                resultado.append(self.ajustes[index].transformar(x[index]))
        return resultado

    def transformar_inv(self, x):
        resultado = []
        for index in range(len(x)):
            if type(x[0]) is np.float64:
                resultado.append((((self.xmax - self.xmin) * x[index]) / (self.max - self.min)) + self.constant_inv)
            else:
                resultado.append(self.ajustes[index].transformar_inv(x[index]))
        return resultado