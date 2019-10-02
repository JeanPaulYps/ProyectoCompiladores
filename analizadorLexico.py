import re
palabrasReservadas = {"si","sinosi","sino","para","mientras","vacio","main"}
patronesTokens = [
('tiposDeDatos',                    r'(entero|cadena|real|bool)'),
    ('variables',                   r'[A-z][\w]*'),
    ('asignacion',                  r'='),
    ('operadorAritmeticos',         r'(\+|\-|(?<!\/)\*(?!\/)|(?<!\*|\/)\/(?!\*|\/)|%)'),
    ('operadorLogico',              r'(&&|\|\||!)'),
    ('operadorRelacional',          r'(==|!=|>|<|>=|<=)'),
    ('saltosDeLineas',              r'\n'),
    ('espacioenblanco',             r'[ \t]+'),
    ('comentarios',                 r'(//[\w\d ]*|/\*[\w\d ]+\*/)'),
    ('terminador',                  r';'),
    ('otrosSimbolos',               r'(,|\(|\)|->|\[|\])'),
    ('repeticion',                  r'(para|mientras)'),
    ('bloques',                     r'[{}]'),
    ('importar',                    r'(importar)'),
    ('clase',                       r'(clase)'),
    ('numeros',                     r'\d+(\.d*)?'),
    ('cadenas',                     r'\"[\w\d ]*\"'),
    ('booleanos',                   r'(Verdadero|Falso)'),
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
