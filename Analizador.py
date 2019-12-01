import csv
from Lexico import Lexico
class Analizador ():
    def __init__(self, tablaTAS,lexico):
        self.tabla = tablaTAS
        self.terminales = tablaTAS[0][:]
        self.producciones = [fila[0] for fila in tablaTAS]
        self.lexico = lexico
        self.pila = ["$", "<S>"]

    @staticmethod
    def leerTablaTAS(nombreArchivo):
        tabla = []
        with open(nombreArchivo, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='|')
            for row in spamreader:
                tabla.append(row)
        return tabla

    @staticmethod
    def obtenerIndice (simbolo, lista):
        try:
            return lista.index(simbolo)
        except:
            return -1

    def hayQueEliminarToken(self, cimaDePila):
        siguienteToken = self.lexico.verSiguienteSimbolo()
        return  siguienteToken == cimaDePila

    def eliminarToken(self):
        self.pila.pop(-1)
        self.lexico.sacarSimbolo()

    def existeProduccion(self, cimaDePila):
        return cimaDePila in self.producciones


    def derivar (self, cimaDePila):
        siguienteToken = self.lexico.verSiguienteSimbolo()
        fila = self.obtenerIndice(cimaDePila, self.producciones)
        columna = self.obtenerIndice(siguienteToken, self.terminales)
        produccion = self.tabla[fila][columna]
        accion = "{} -> {}".format(cimaDePila, produccion)
        self.pila.pop(-1)
        if produccion != "?":
            for simbolo in self.obtenerSimbolos(produccion): 
                self.pila.append(simbolo)
        return accion

    def sePuedeDerivar (self, cimaDePila):
        siguienteToken = self.lexico.verSiguienteSimbolo()
        fila = self.obtenerIndice(cimaDePila, self.producciones)
        columna = self.obtenerIndice(siguienteToken, self.terminales)
        if fila == -1 or columna == -1:
            return False
        produccion = self.tabla[fila][columna]  
        if not produccion:
            return False
        return True

    def analizar(self):
        self.estados = []
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
                self.eliminarToken()
            elif self.existeProduccion(cimaDePila) and self.sePuedeDerivar(cimaDePila):
                accion = self.derivar(cimaDePila)
            else:
                print(siguienteToken)
                self.estados.append((pila,simbolos, "ERROR"))
                print("Error de sintaxis")
                break
            if siguienteToken == "$" and cimaDePila == "$":
                accion = "ACEPTAR"
                print("ACEPTAR")
            #self.estados.append(( " ".join(pila) ,siguienteToken, accion))
            self.estados.append(( " ".join(pila) ,simbolos, accion))
    

    @staticmethod
    def obtenerSimbolos (produccion):
        return produccion.split(" ")[::-1]



f = open ('prueba.txt','r')
entrada = f.read()
f.close()
lexico = Lexico(entrada)

for i in lexico.tokens:
    print(i)

a = Analizador(Analizador.leerTablaTAS("tablaTAS.csv"), lexico)
a.analizar()

f2 = open("salida.txt", "w")
for i1,i2,i3 in a.estados:
   f2.write("{}\t{}\t{}\n".format(i1,i2,i3))
f2.close()

