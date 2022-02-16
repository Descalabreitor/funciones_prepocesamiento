class CodificadorEtiqueta:

    def __init__(self):
        self.codification = {}
        self.inv_codification = {}

    def ajustar(self,y):
        resultado = {}
        n = 0
        for sim_val in y:
            if sim_val in resultado.keys():
                continue
            resultado[sim_val] = n
            n+=1
        self.codification = resultado
        self.inv_codification = {v:k for k,v in resultado.items()}
        return resultado

    def transformar(self,y):
        resultado = []
        for sim_val in y:
            if sim_val in self.codification.keys():
                resultado.append(self.codification[sim_val])
            else:
                raise ValueError(str(sim_val)+" doesn´t exist in codification")
        return resultado

    def transformar_inv(self,y):
        resultado = []
        for code in y:
            if code in self.inv_codification.keys():
                resultado.append(self.inv_codification[code])
            else:
                raise ValueError("Code "+str(code)+" doesn´t have a simbolic value")
        return resultado