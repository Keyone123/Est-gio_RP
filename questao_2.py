def contar(string):
    cont = string.lower().count('a')
    if cont > 0:
        return f'A letra "a" aparece {cont} vezes na string'
    else:
        return 'A letra "a" não aparece na string'

string = input('Digite uma string: ')
print(contar(string))
