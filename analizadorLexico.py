import re
palabrasReservadas = {"si","sinosi","sino","para","mientras","vacio","main"}
patronesTokens = [
    ('palabrasReservadas',          r'(si|sinosi|sino|para|mientras|vacio|main)'),
    ('tiposDeDatos',                r'(entero|cadena|real|bool)'),
    ('repeticion',                  r'(para|mientras)'),
    ('importar',                    r'(importar)'),
    ('clase',                       r'(clase)'),
    ('booleanos',                   r'(Verdadero|Falso)'),
    ('variables',                   r'[A-z][\w]*'),
    ('asignacion',                  r'(=|->)'),
    ('operadorAritmeticos',         r'(\+|\-|(?<!\/)\*(?!\/)|(?<!\*|\/)\/(?!\*|\/)|%)'),
    ('operadorLogico',              r'(&&|\|\||!)'),
    ('operadorRelacional',          r'(==|!=|>|<|>=|<=)'),
    ('saltosDeLineas',              r'\n'),
    ('espacioenblanco',             r'[ \t]+'),
    ('comentarios',                 r'(//[\w\d ]*|/\*[\w\d \n]+\*/)'),
    ('terminador',                  r';'),
    ('otrosSimbolos',               r'(,|\(|\)|\[|\])'),
    ('bloques',                     r'[{}]'),
    ('numeros',                     r'\d+(\.d*)?'),
    ('cadenas',                     r'\"[\w\d ]*\"'),
    ('caracter',                    r'\"[\w\d ]?\"'),
    ('ERROR',                       r'.'),
]

def analizadorLexico():
    pass

def obtenerTokensRegex ():
    return '|'.join('(?P<%s>%s)' % pair for pair in patronesTokens)

def prueba():
    tokensRegex = obtenerTokensRegex()
    print(tokensRegex)

TokensRegex = obtenerTokensRegex()
codigo = open("prueba.txt",'r')
codigo = codigo.read()
for i in re.finditer(TokensRegex, codigo):
    print(i, i.lastgroup)
