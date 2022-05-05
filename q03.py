#Declaração de variaveis
A = []
B = []
C = []
D = []
inicio = 87
parar = 5396
ultimo = parar + 1
for i in range(inicio, ultimo):
    A.append(i)
print(A)
for i in A:
    B.append(i * 8)
    C.append(B[-1] - 42)
    D.append((C[-1]**B[-1])//i)
print(B)
print(C)
print(D)
