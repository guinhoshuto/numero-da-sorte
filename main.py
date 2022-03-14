from collections import deque

#TODO
# - limite de min e máx do número
# - não deixar que o número mais alto fique muito mais baixo que o máximo
# - gerar o tanto de números necessários, não o número de letras da palavra
#ideia: embaralhar string alfabeto baseado na palavra
alfabeto = "abcdefghijklmnopqrstuvwxyz"
def embaralha(palavra):
    c = deque(list(alfabeto))
    i = 0
    shift = 0
    letras = list(palavra)
    for l in letras:
        shift += alfabeto.find(l)

    c.rotate(shift)
    codigo = list(c)
     
    return codigo

def criptografa(palavra, n):
    #coloca uma sequência de números pra palavra 
    index = 0
    codigo = embaralha(palavra)
    numeros = []
    letras = list(palavra)
    print(letras)
    for l in letras: 
        numeros.append(codigo.index(l) + index)
        index += 1

    numeros.sort()
    #retorna array de números
    return numeros

print(embaralha("padre"))
print(criptografa("padre", 1))