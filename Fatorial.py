# Calculando o Fatorial de qualquer número!
import numpy
num = eval(input('Digite o numero que será calculado: '))
fatorial = []


def subtrair():
    contador = num
    while contador > 1:
        contador -= 1
        if contador == 0:
            continue
        fatorial.append(contador)


subtrair()
# Usando um laço ***FOR***
multi = 1
for i in fatorial:
    multi *= i
res = num * multi

#Importando a Biblioteca NUMPY
produto = numpy.prod(fatorial)
resultado = num * produto


print(f'O fatoriarl de {num}! é {resultado}')
print(res)
