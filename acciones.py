from TablaDeSimbolos import TablaDeSimbolos
from Variable import Variable
from Triplete import Triplete
import re


palabrasReservadas = ["si","sino","sinosi","para","mientras","vacio","main",
                          "importar","real","cadena","bool","caracter","leer",
                          "imprimir","clase","entero","verdadero","falso", "retornar"]

def obtenerTipoCadena (cadena):
  if re.fullmatch(r"\d+(\.\d+)?", cadena):
    if "." in cadena:
      return "real"
    else:
      return "entero"
  elif cadena == "verdadero":
    return "bool"
  elif cadena == "falso":
    return "bool"
  else:
    return "cadena"


def obtenerValorMatematico(simbolo, interprete):
  print(type(simbolo))
  if isinstance(simbolo, str):
    if esID(simbolo):
      tabla = obtenerTablaActual(interprete)
      variable = tabla.buscarSimbolo(simbolo)
      return variable.valor
    else:
      return eval(simbolo)
  if isinstance(simbolo, Triplete):
      return simbolo.resultado

def convertir(cadena):
  if re.fullmatch(r"'\d+(\.\d+)?'", cadena):
    if "." in cadena:
      return int(cadena)
    else:
      return float(cadena)
  elif cadena == "verdadero":
    return cadena
  elif cadena == "falso":
    return cadena
  else:
    return cadena

def esTriplete (simbolo):
  return isinstance(simbolo, Triplete)

def esID (simbolo):
  if re.fullmatch(r"[a-zA-Z][\w]*", simbolo) and\
    not simbolo in palabrasReservadas:
    return True
  else:
    return False

def obtenerValor (simbolo):
  if re.match(r'\d+(\.\d+)?', simbolo):
    if "." in simbolo:
      return float(simbolo)
    else:
      return int(simbolo)
  elif re.match(r'\"[\w\d ]*\"', simbolo) or \
    re.match(r'\"[\w\d ]*\"', simbolo):
    return simbolo
  elif simbolo == "verdadero":
    return simbolo
  elif simbolo == "falso":
    return simbolo


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

#A cada asinacion se debe saber si es un valor
#O es una variable  
def asignar (interprete, triplete):
  tabla = obtenerTablaActual(interprete)
  variable = triplete.arg1
  variable = tabla.buscarSimbolo(variable)
  simbolo = triplete.arg2
  if esTriplete(simbolo):
      if variable.tipo == "real":
        variable.valor = float(simbolo.resultado)
      else:
        variable.valor = simbolo.resultado
  elif esID(simbolo):
    otraVariable = tabla.buscarSimbolo(simbolo)
    if variable.tipo == "real" and \
      otraVariable.tipo == "entero":
      variable.valor = float(otraVariable.valor)
    else:
      variable.valor = otraVariable.valor
  else:
    variable.valor = obtenerValor(simbolo)

def imprimir (interprete, triplete):
  tabla = obtenerTablaActual(interprete)
  variable = triplete.arg1
  variable = tabla.buscarSimbolo(variable)
  print(variable.valor)


def leer (interprete, triplete):
  tabla = obtenerTablaActual(interprete)
  variable = triplete.arg1
  variable = tabla.buscarSimbolo(variable)
  entrada = input()
  if variable.tipo == obtenerTipoCadena(entrada):
      triplete.resultado = entrada
  else:
    raise TypeError("No son del mismo tipo")



def sumar (interprete, triplete):
  operador1 = obtenerValorMatematico(triplete.arg1, interprete)
  operador2 = obtenerValorMatematico(triplete.arg2, interprete)
  triplete.resultado = operador1 + operador2

def sumar (interprete, triplete):
  operador1 = obtenerValorMatematico(triplete.arg1, interprete)
  operador2 = obtenerValorMatematico(triplete.arg2, interprete)
  triplete.resultado = operador1 + operador2

def restar (interprete, triplete):
  operador1 = obtenerValorMatematico(triplete.arg1, interprete)
  operador2 = obtenerValorMatematico(triplete.arg2, interprete)
  triplete.resultado = operador2 - operador1

def multiplicar (interprete, triplete):
  operador1 = obtenerValorMatematico(triplete.arg1, interprete)
  operador2 = obtenerValorMatematico(triplete.arg2, interprete)
  triplete.resultado = operador2 * operador1

def dividir (interprete, triplete):
  operador1 = obtenerValorMatematico(triplete.arg1, interprete)
  operador2 = obtenerValorMatematico(triplete.arg2, interprete)
  triplete.resultado = operador2 / operador1

accion = {"crearAlcance": crearAlcance,
          "borrarAlcance": borrarAlcance,
          "inicio": inicio,
          "fin": fin,
          "crearVariable": crearVariable,
          "asignar": asignar,
          "imprimir": imprimir,
          "leer": leer,
          "sumar": sumar,
          "restar": restar,
          "multiplicar": multiplicar,
          "dividir": dividir
        }