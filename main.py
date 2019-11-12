from Lexico import Lexico

codigo = open("prueba.txt",'r')
codigo = codigo.read()
Tokens = Lexico(codigo)
for i, j in Tokens.tokens:
    print(i,j)
for i in Tokens.tablaDeSimbolos:
    print(i)

print(Tokens.verSiguienteSimbolo())
print(Tokens.sacarSimbolo())
print(Tokens.verSiguienteSimbolo())