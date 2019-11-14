import re

"""
Analizador lexico del lenguaje
"""

class Lexico():
    tablaDeSimbolos = []
    palabrasReservadas = ["si","sino","sinosi","para","mientras","vacio","main",
                          "importar","real","cadena","bool","caracter","leer",
                          "imprimir","clase","entero","verdadero","falso", "retornar"]
    patronesTokens = [
        ('ID',                          r'[a-zA-Z][\w]*'),
        ('asignacion',                  r'(=(?!=)|->)'),
        ('operadorAritmetico',          r'(\+|\-|(?<!\/)\*(?!\/)|(?<!\*|\/)\/(?!\*|\/)|%)'),
        ('operadorLogico',              r'(&&|\|\|)'),
        ('operadorRelacional',          r'(==|!=|>(?!=)|<(?!=)|>=|<=)'),
        ('saltoDeLinea',                r'\n'),
        ('espacioenblanco',             r'[ \t]+'),
        ('comentario',                  r'\/\*(\*(?!\/)|[^*])*\*\/|\/\/.*'),
        ('simbolo',                     r'(,|\(|\)|\[|\])|;|\{|\}|\.'),
        ('numero',                      r'\d+(\.d*)?'),
        ('cadena',                      r'\"[\w\d ]*\"'),
        ('caracter',                    r'\"[\w\d ]?\"'),
        ('DESCONOCIDO',                 r'.'),
    ]

    def __init__(self, codigo):
        self.tokens = self.obtenerTokens(codigo)
        self.tokens.append(("$", "EOF"))

    def obtenerTokensRegex (self):
        return '|'.join('(?P<%s>%s)' % pair for pair in self.patronesTokens)

    def obtenerTokens (self, codigo):
        codigo = codigo.replace("\r", "\n")
        tokensRegex = self.obtenerTokensRegex()
        tokens = []
        for token in re.finditer(tokensRegex, codigo):
            tipo = token.lastgroup
            valor = token.group()
            
            if tipo == 'espacioenblanco' or tipo == "saltoDeLinea" or  tipo == "comentario":
                pass
            else:
                if tipo == "ID" and valor in self.palabrasReservadas:
                    tipo = "palabraReservada"
                elif tipo == "ID" and valor not in self.tablaDeSimbolos:
                    self.tablaDeSimbolos.append(valor)
                tokens.append((valor,tipo))
        return tokens

    def verSiguienteSimbolo(self):
        siguienteToken = self.tokens[0][0]
        tipoToken = self.tokens[0][1]
        if tipoToken == "ID":
            return "ID"
        elif tipoToken == "numero" \
            or tipoToken == "cadena" \
            or tipoToken == "caracter":
            return "VALOR"
        return siguienteToken

    def sacarSimbolo(self):
        return self.tokens.pop(0)

    def obtenerPilaSimbolos(self):
        return [token[0] for token in self.tokens]