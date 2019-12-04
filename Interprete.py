from Triplete import Triplete
from TablaDeSimbolos import TablaDeSimbolos
from acciones import accion

class Interprete():
    
    def __init__(self):
        self.tripletes = Triplete.tripletes
        self.tablaDeSimbolosGlobal = TablaDeSimbolos()
        self.tablaDeSimbolosActual = self.tablaDeSimbolosGlobal

    
    def ejecutar (self):
        if self.tripletes[0].accion == "inicio" and \
             self.tripletes[-1].accion == "fin":
            for triplete in self.tripletes:
                accion[triplete.accion](self, triplete)
        