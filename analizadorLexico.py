import re
patronesTokens = [
    ('palabrasReservada',           r'(si|sinosi|sino|para|mientras|vacio|main)'),
    ('tiposDeDato',                 r'(entero|cadena|real|bool)'),
    ('repeticion',                  r'(para|mientras)'),
    ('importar',                    r'(importar)'),
    ('clase',                       r'(clase)'),
    ('booleano',                    r'(Verdadero|Falso)'),
    ('variable',                    r'[A-z][\w]*'),
    ('asignacion',                  r'(=|->)'),
    ('operadorAritmetico',          r'(\+|\-|(?<!\/)\*(?!\/)|(?<!\*|\/)\/(?!\*|\/)|%)'),
    ('operadorLogico',              r'(&&|\|\||!)'),
    ('operadorRelacional',          r'(==|!=|>|<|>=|<=)'),
    ('saltoDeLinea',                r'\n'),
    ('espacioenblanco',             r'[ \t]+'),
    ('comentario',                  r'(//[\w\d ]*|/\*[\w\d \n]+\*/)'),
    ('terminador',                  r';'),
    ('otrosSimbolo',                r'(,|\(|\)|\[|\])'),
    ('bloque',                      r'[{}]'),
    ('numero',                      r'\d+(\.d*)?'),
    ('cadena',                      r'\"[\w\d ]*\"'),
    ('caracter',                    r'\"[\w\d ]?\"'),
    ('ERROR',                       r'.'),
]

def obtenerTokensRegex ():
    return '|'.join('(?P<%s>%s)' % pair for pair in patronesTokens)

def obtenerTokens (codigo):
    codigo = codigo.replace("\r", "\n")
    tokensRegex = obtenerTokensRegex()
    tuplasTokens = []
    for tokens in re.finditer(tokensRegex, codigo):
        tipo = tokens.lastgroup
        valor = tokens.group()
        if tipo == 'espacioenblanco' or tipo == "saltoDeLinea":
            pass
        elif tipo == 'ERROR':
            tuplasTokens.append((valor,tipo)) 
            return tuplasTokens
        else:
            tuplasTokens.append((valor,tipo))
    return tuplasTokens
        
"""codigo = open("prueba.txt",'r')
codigo = codigo.read()
Tokens = obtenerTokens(codigo)
for i, j in Tokens:
    print(i,j)"""
