from Analizador import Analizador
from TablaDeSimbolos import TablaDeSimbolos
from Simbolo import Simbolo
from accionesSemanticas import reglas
import re

class Semantico (Analizador):
    def __init__(self, tablaTAS, lexico):
        super().__init__(tablaTAS, lexico)
        self.pilaSemantica = []
        self.tablaDeSimbolosGlobal = TablaDeSimbolos()
        self.tablaDeSimbolosActual = self.tablaDeSimbolosGlobal
        self.token = ""

    @staticmethod
    def esRegla(cimaDePila):
        return re.match(r"{\S*}", cimaDePila)

    @staticmethod
    def obtenerRegla (regla):
        return regla[1:-1]

    def analisisSemantico(self):
        self.estados = []
        self.token = self.lexico.verSiguienteToken()
        siguienteToken = self.lexico.verSiguienteSimbolo()
        cimaDePila = self.pila[-1]
        accion = ""
        while siguienteToken != "$" or cimaDePila != "$":
            #print("{}\t\t{}".format(self.pila,self.lexico.obtenerPilaSimbolos()))
            pila = self.pila[:]
            simbolos = self.lexico.obtenerPilaSimbolos()
            siguienteToken = self.lexico.verSiguienteSimbolo()
            cimaDePila = self.pila[-1]
            accion = ""
            if self.hayQueEliminarToken(cimaDePila):
                self.token = self.lexico.verSiguienteToken()
                self.eliminarToken()
            elif self.existeProduccion(cimaDePila) and self.sePuedeDerivar(cimaDePila):
                accion = self.derivar(cimaDePila)
            elif self.esRegla(cimaDePila):
                regla = self.obtenerRegla(cimaDePila)
                #reglas[regla]
                #print(self.token, regla)
                reglas[regla](self)
                self.pila.pop(-1)
            else:
                print(siguienteToken, cimaDePila, self.sePuedeDerivar(cimaDePila))
                self.estados.append((pila,simbolos, "ERROR"))
                print("Error de sintaxis")
                break
            if siguienteToken == "$" and cimaDePila == "$":
                accion = "ACEPTAR"

                print("ACEPTAR")
                reglas["fin"](self)
            
            #self.estados.append(( " ".join(pila) ,siguienteToken, accion))
            #self.estados.append(( " ".join(pila) ,simbolos, accion))
    