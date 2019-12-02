import re
from Token import Token

"""
Analizador lexico del lenguaje
"""

class Lexico():
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
        ('numero',                      r'\d+(\.\d+)?'),
        ('cadena',                      r'\"[\w\d ]*\"'),
        ('caracter',                    r'\"[\w\d ]?\"'),
        ('DESCONOCIDO',                 r'.'),
    ]

    def __init__(self, codigo):
        self.tokens = self.obtenerTokens(codigo)
        self.tokens.append(Token("$", "EOF"))

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
                if tipo == "numero":
                    if "." in valor:
                        tipo = "real"
                    else:
                        tipo = "entero"
                tokens.append(Token(valor,tipo))
        return tokens

    def verSiguienteSimbolo(self):
        token = self.tokens[0]
        if token.tipo == "ID":
            return "ID"
        elif token.tipo == "entero" \
            or token.tipo == "real" \
            or token.tipo == "cadena" \
            or token.tipo == "caracter":
            return "VALOR"
        return token.valor

    def sacarSimbolo(self):
        return self.tokens.pop(0)

    def obtenerPilaSimbolos(self):
        return [token.valor for token in self.tokens]

f = open ('prueba.txt','r')
entrada = f.read()
f.close()
lexico = Lexico(entrada)

for i in lexico.tokens:
    print(i)

print(lexico.verSiguienteSimbolo())