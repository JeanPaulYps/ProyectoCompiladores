import csv
class Analizador ():
    def __init__(self, tablaTAS,programa):
        self.tabla = tablaTAS
        self.terminales = tablaTAS[0][:]
        self.producciones = [fila[0] for fila in tablaTAS]
        self.programa = programa
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
        return lista.index(simbolo)

    def analizarPrograma(self):
        siguienteToken = self.programa[0]
        cimaDePila = self.pila[-1]
        
        while siguienteToken != "$" or cimaDePila != "$":
            print("{}\t\t{}".format(self.pila,self.programa))
            siguienteToken = self.programa[0]
            cimaDePila = self.pila[-1]
            if siguienteToken == cimaDePila:
                self.pila.pop(-1)
                self.programa.pop(0)
            elif cimaDePila in self.producciones:
                fila = self.obtenerIndice(cimaDePila, self.producciones)
                columna = self.obtenerIndice(siguienteToken, self.terminales)
                produccion = self.tabla[fila][columna]
                self.pila.pop(-1)
                if not produccion:
                    print("ERROR")
                    break
                if produccion != "&":
                    for simbolo in self.obtenerSimbolos(produccion): 
                        self.pila.append(simbolo)
            else:
                print("ERROR")
                break
            cimaDePila = self.pila[-1]
            siguienteToken = self.programa[0]
        
        print("{}\t\t{}".format(self.pila,self.programa))
        if siguienteToken == "$":
            print("ACEPTAR")
        else:
            print("ERROR")

    @staticmethod
    def obtenerSimbolos (produccion):
        return produccion.split(" ")[::-1]


    


entrada = ["while", "id", "{", "while", "id", "{","}", "}","$"]
a = Analizador(Analizador.leerTablaTAS("EjemploClase.csv"), entrada)
a.analizarPrograma()