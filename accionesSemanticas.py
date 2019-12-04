from Triplete import Triplete
from TablaDeSimbolos import TablaDeSimbolos
from Variable import Variable
from Token import Token
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

def tieneValor(simbolo):
  if isinstance(simbolo, Token):
    if simbolo.valor == "verdadero" or \
      simbolo.valor == "falso" or \
      simbolo.tipo == "entero" or \
      simbolo.tipo == "real"  or\
      simbolo.tipo == "cadena"  or\
      simbolo.tipo == "caracter" :
      return True
  elif isinstance(simbolo, Variable):
    return simbolo.valor


def obtenerTipo (simbolo):
  if isinstance(simbolo, Token):
    return simbolo.tipo
  elif isinstance(simbolo, Variable):
    return simbolo.tipo
  else:
    raise NameError("No se puede obtener tipo")

def obtenerValor (simbolo):
  if isinstance(simbolo, Token):
    return simbolo.valor
  elif isinstance(simbolo, Variable):
    return simbolo.valor
  else:
    raise NameError("No se puede obtener valor")


def verificarTipo (tipoEsperado, tipoDeVariable):
  tipoV = obtenerTipo(tipoDeVariable)
  tipoE = obtenerTipo(tipoEsperado)
  print(f"tipoV: {tipoV} tipoE: {tipoE} ")
  if tipoE == "real" and tipoV == "entero":
    return True
  return tipoE == tipoV


def obtenerTablaActual (semantico):
  return semantico.tablaDeSimbolosActual

def determinarSimbolo(semantico, token):
  if tieneValor(token):
    return token
  elif token.tipo == "ID":
    tabla =obtenerTablaActual(semantico)
    return  tabla.buscarSimbolo(token.valor)
  else:
    raise NameError("No se puede obtener valor") 

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

def asignar (semantico):
  tabla = obtenerTablaActual(semantico)
  tokenValor = pop(semantico)
  tokenVariable = pop(semantico)
  valor = determinarSimbolo(semantico, tokenValor)
  variable = determinarSimbolo(semantico, tokenVariable)
  print(f"tipoValor {type(valor)} tipoVariable {type(variable)}")
  if not variable:
    raise NameError("No existe simbolo")
  if verificarTipo(variable, valor):
    variable.valor = True
    Triplete("asignar", tokenVariable.valor, tokenValor.valor)
  else:
    raise NameError("No se puede asignar ese valor")
  print(str(tabla.buscarSimbolo(variable.nombre)))
  




reglas = {"crearAlcance": crearAlcance,
          "borrarAlcance": borrarAlcance,
          "inicio": inicio,
          "fin": fin,
          "push": push,
          "pop": pop,
          "crearVariable": crearVariable,
          "asignar": asignar
        }