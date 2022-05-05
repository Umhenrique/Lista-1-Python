#Declaração de variaveis
lista = []
somaq = 0

for i in range(5):
    lista.append(int(input()))
    somaq += lista[i] ** 2
print(somaq)
