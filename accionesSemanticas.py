from Triplete import Triplete
from TablaDeSimbolos import TablaDeSimbolos
from Variable import Variable
"""
def generarTripletes(funcion):
  def agregarTriplete(*args, **kwargs):
    res = funcion(*args)
    if res:
      argumento1, argumento2 = args
      Triplete((funcion.__name__,  argumento1, argumento2 ), res)
      return True
    else:
      return False

  return agregarTriplete

@generarTripletes
def sumar (operando1, operando2):
  return operando1 + operando2

@generarTripletes
def restar (operando1, operando2):
  return operando1 - operando2

@generarTripletes
def verificarTipo (tipoEsperado, tipoDeVariable):
  return tipoEsperado == tipoDeVariable"""

def obtenerTablaActual (semantico):
  return semantico.tablaDeSimbolosActual

def crearAlcance (semantico):
  tabla = obtenerTablaActual(semantico)
  semantico.tablaDeSimbolosActual = tabla
  Triplete("crearAlcance")

def borrarAlcance (semantico):
  tabla = obtenerTablaActual(semantico)
  semantico.tablaDeSimbolosActual = semantico.tablaDeSimbolosActual.padre
  del(tabla)
  Triplete("borrarAlcance")

def inicio (semantico):
  Triplete("inicio")

def fin (semantico):
  Triplete("fin")

def push (semantico):
  token = semantico.token
  semantico.pilaSemantica.append(token)

def pop (semantico):
  return semantico.pilaSemantica.pop(-1)
  

def peek (semantico):
  return semantico.pilaSemantica[-1]

def crearVariable (semantico):
  tabla = obtenerTablaActual(semantico)
  token = pop(semantico)
  tipo = peek(semantico)
  variable = Variable(token.valor, tipo.valor)
  tabla.agregarSimbolo(variable)
  Triplete("crearVariable", tipo.valor, token.valor)



reglas = {"crearAlcance": crearAlcance,
          "borrarAlcance": borrarAlcance,
          "inicio": inicio,
          "fin": fin,
          "push": push,
          "pop": pop,
          "crearVariable": crearVariable

        }