from TablaDeSimbolos import TablaDeSimbolos
from Variable import Variable
import re


palabrasReservadas = ["si","sino","sinosi","para","mientras","vacio","main",
                          "importar","real","cadena","bool","caracter","leer",
                          "imprimir","clase","entero","verdadero","falso", "retornar"]

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
  print(variable, simbolo)
  if esID(simbolo):
    otraVariable = tabla.buscarSimbolo(simbolo)
    if variable.tipo == "real" and \
      otraVariable.tipo == "entero":
      variable.valor = float(otraVariable.valor)
    else:
      variable.valor = otraVariable.valor
  else:
    variable.valor = obtenerValor(simbolo)
  print(variable)


accion = {"crearAlcance": crearAlcance,
          "borrarAlcance": borrarAlcance,
          "inicio": inicio,
          "fin": fin,
          "crearVariable": crearVariable,
          "asignar": asignar
        }