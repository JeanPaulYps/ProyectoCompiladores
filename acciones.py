from TablaDeSimbolos import TablaDeSimbolos
from Variable import Variable

def obtenerTablaActual (interprete):
  return interprete.tablaDeSimbolosActual 

def crearAlcance (interprete, triplete):
  tabla = TablaDeSimbolos(interprete.tablaDeSimbolosActual)
  interprete.tablaDeSimbolosActual = tabla

def borrarAlcance (interprete, triplete):
  tabla = obtenerTablaActual(interprete)
  interprete.tablaDeSimbolosActual = interprete.tablaDeSimbolosActual.padre
  del(tabla)

def inicio (interprete, triplete):
    pass

def fin (interprete, triplete):
    pass

def crearVariable (interprete, triplete):
  tipo = triplete.arg1
  valor = triplete.arg2
  tabla = obtenerTablaActual(interprete)
  variable = Variable(valor, tipo)
  tabla.agregarSimbolo(variable)


accion = {"crearAlcance": crearAlcance,
          "borrarAlcance": borrarAlcance,
          "inicio": inicio,
          "fin": fin,
          "crearVariable": crearVariable
        }