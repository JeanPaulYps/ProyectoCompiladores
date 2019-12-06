import re
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

def esTriplete(simbolo):
  return isinstance(simbolo, Triplete)

def esToken(simbolo):
  return isinstance(simbolo, Token)

def esVariable(simbolo):
  return isinstance(simbolo, Variable)

def obtenerResultadoMat (simbolo1, simbolo2):
  tipo1 = obtenerTipo(simbolo1)
  tipo2 = obtenerTipo(simbolo2)
  if tipo1 == tipo2:
    return tipo1
  else:
    return "real"



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
    if simbolo.tipo == "cadena" and \
      re.fullmatch(r'\"[\w\d ]?\"', simbolo.valor):
      return "caracter"
    if simbolo.valor == "verdadero" or \
      simbolo.valor == "falso":
      return "bool"
    return simbolo.tipo
  elif isinstance(simbolo, Variable):
    return simbolo.tipo
  elif esTriplete(simbolo):
    return simbolo.resultado
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
  if tipoE == "real" and tipoV == "entero":
    return True
  if tipoE == "cadena" and tipoV == "caracter":
    return True
  return tipoE == tipoV


def obtenerTablaActual (semantico):
  return semantico.tablaDeSimbolosActual

def determinarSimbolo(semantico, token):
  if tieneValor(token) or esTriplete(token):
    return token
  elif token.tipo == "ID":
    tabla = obtenerTablaActual(semantico)
    return tabla.buscarSimbolo(token.valor)
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
  print(tokenValor)
  if not variable:
    raise NameError("No existe simbolo")
  if verificarTipo(variable, valor):
    variable.valor = True
    if tieneValor(valor):
      Triplete("asignar", tokenVariable.valor, tokenValor.valor)
    elif esTriplete(tokenValor):
      Triplete("asignar", tokenVariable.valor, tokenValor)
    else:
      raise NameError("No tiene valor")
  else:
    raise NameError("No se puede asignar ese valor")
  
def imprimir (semantico):
  tabla = obtenerTablaActual(semantico)
  tokenVariable = pop(semantico)
  variable = determinarSimbolo(semantico, tokenVariable)
  if not variable:
    raise NameError("No existe simbolo")
  if variable.valor:
    Triplete("imprimir", variable.nombre, None)
  else:
    raise  NameError("Esa variable no tiene dato")

def leer (semantico):
  tabla = obtenerTablaActual(semantico)
  tokenVariable = pop(semantico)
  variable = determinarSimbolo(semantico, tokenVariable)
  if not variable:
    raise NameError("No existe simbolo")
  variable.valor = True
  t = Triplete("leer", variable.nombre, None)
  Triplete("asignar", variable.nombre, t)

def obtenerOperando(semantico, operando):
  if esToken(operando):
    return determinarSimbolo(semantico, operando)
  elif esTriplete(operando):
    return operando

def obtenerValorParaOperar(operando):
  if esToken(operando):
    return operando.valor
  elif esVariable(operando):
    return operando.nombre
  elif esTriplete(operando):
    return operando

def sumar (semantico):
  operando1 = obtenerOperando(semantico, pop(semantico))
  operando2 = obtenerOperando(semantico, pop(semantico))
  if verificarTipo(operando1, operando2):
    resultado = obtenerResultadoMat(operando1, operando2)
    op1 = obtenerValorParaOperar(operando1)
    op2 = obtenerValorParaOperar(operando2)
    t = Triplete("sumar", op1, op2, resultado)
    semantico.pilaSemantica.append(t)
  else:
    raise TypeError("No son compatibles")


  
    



reglas = {"crearAlcance": crearAlcance,
          "borrarAlcance": borrarAlcance,
          "inicio": inicio,
          "fin": fin,
          "push": push,
          "pop": pop,
          "crearVariable": crearVariable,
          "asignar": asignar,
          "imprimir": imprimir,
          "leer": leer,
          "sumar": sumar
        }