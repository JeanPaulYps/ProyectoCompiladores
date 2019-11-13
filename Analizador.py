import csv
from Lexico import Lexico
class Analizador ():
    def __init__(self, tablaTAS,lexico):
        self.tabla = tablaTAS
        self.terminales = tablaTAS[0][:]
        self.producciones = [fila[0] for fila in tablaTAS]
        self.lexico = lexico
        self.pila = ["$", "S"]

    @staticmethod
    def leerTablaTAS(nombreArchivo):
        tabla = []
        with open(nombreArchivo, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                tabla.append(row)
        return tabla

    @staticmethod
    def obtenerIndice (simbolo, lista):
        try:
            return lista.index(simbolo)
        except:
            return -1
            

    def analizar(self):
        self.estados = []
        siguienteToken = self.lexico.verSiguienteSimbolo()
        cimaDePila = self.pila[-1]
        accion = ""
        while siguienteToken != "$" or cimaDePila != "$":
            print("{}\t\t{}".format(self.pila,self.lexico.obtenerPilaSimbolos()))
            pila = self.pila[:]
            simbolos = self.lexico.obtenerPilaSimbolos()
            siguienteToken = self.lexico.verSiguienteSimbolo()
            cimaDePila = self.pila[-1]
            accion = ""
            if siguienteToken == cimaDePila:
                self.pila.pop(-1)
                self.lexico.sacarSimbolo()
            elif cimaDePila in self.producciones:
                fila = self.obtenerIndice(cimaDePila, self.producciones)
                columna = self.obtenerIndice(siguienteToken, self.terminales)
                if fila == -1 or columna == -1:
                    self.estados.append((pila,simbolos, "ERROR"))
                    print("ERROR")
                    break
                produccion = self.tabla[fila][columna]
                accion = "{} -> {}".format(cimaDePila, produccion)
                self.pila.pop(-1)
                if not produccion:
                    self.estados.append((pila,simbolos, "ERROR"))
                    print("ERROR")
                    break
                if produccion != "&":
                    for simbolo in self.obtenerSimbolos(produccion): 
                        self.pila.append(simbolo)
            else:
                self.estados.append((pila,simbolos, "ERROR"))
                print("ERROR")
                break
            if siguienteToken == "$" and cimaDePila == "$":
                accion = "ACEPTAR"
            self.estados.append((pila,simbolos, accion))
        

    @staticmethod
    def obtenerSimbolos (produccion):
        return produccion.split(" ")[::-1]


    
"""
entrada = ["while", "id", "{", "while", "id", "{","}", "}","$"]
entrada = "while  a { while a {}}"
lexico = Lexico(entrada)
print(lexico.tokens)
a = Analizador(Analizador.leerTablaTAS("EjemploClase.csv"), lexico)
a.analizar()
for i in a.estados:
    print(i)"""