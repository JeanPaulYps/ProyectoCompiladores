from Marcador import Marcador

class Triplete ():
  tripletes = []
  marcadores = []

  def __init__(self, accion, arg1 = None, arg2 = None, resultado = None):
    self.accion = accion
    self.arg1 = arg1
    self.arg2 = arg2
    self.resultado = resultado
    self.ID = len(self.tripletes)
    self.tripletes.append(self)
  
  def __str__ (self):
    return "Triplete: ({}, {}, {})  Resultado: {} ".format(self.accion, self.arg1, self.arg2, self.resultado)

  @staticmethod
  def agregarMarcador():
    numeroMarcador = Marcador(len(Triplete.tripletes))
    triplete = (Marcador, numeroMarcador, None)
    resultado = numeroMarcador
    Triplete(triplete, resultado)

        

  @staticmethod
  def tripletesAcadena():
    resultado = ""
    for i,triplete in enumerate(Triplete.tripletes):
      resultado = resultado + f"{str(triplete)}\n"
    return resultado