import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #arredonda a raiz pra cima, pra não dar um número muito grande 
#ou: print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#ou posso usar a função math pra importar sqrt

#from math import sqrt
#num = int(input("Digite um número: "))
#raiz = sqrt(num)                                              não preciso usar o math.sqrt
#print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#ou posso usar o floor pra arredondar a raíz pra baixo
#from math import sqrt, floor
#num = int(input("Digite um número: "))
#raiz = sqrt(num)                                             
#print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

import random
numero = random.random()
print(numero)      #vai me gerar um número entre 0 e 1

#se eu quiser um número aleatório de 1 a 10, eu coloco:
import random
numero = random.randint(1,10)
print(numero)      

#posso importar outros módulos, instalar no computador e começar a usar

#=======================================================================================================

#desafio 16 - crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira, ex.: a parte inteira
#do número 6.127 é 6
import math
numReal = float(input("Insira um número real para saber sua parte inteira: "))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(numReal, math.trunc(numReal)))
#ou posso usar from math import trunc, e tirar o math que usei na linha de cima
#ou posso fazer sem importar biblioteca, da seguinte forma:
#numReal = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(numReal, int(numReal)))

#========================================================================================================

#desafio 17 - faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
#e mostre o comprimento da hipotenusa 
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1/2) #elevo a 1/2 pra calcular a raiz quadrada desse valor todo
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

#agora usando a importação math:

#import math
#oposto = float(input('Comprimento do cateto oposto: '))
#adjacente = float(input('Comprimento do cateto adjacente: '))
#hipotenusa = math.hypot(oposto, adjacente)
#print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
#como estou usando só o hypot posso usar -> from math import hypot e tirar o math da fórmula da hipotenusa

#==================================================================================================================

#desaio 18 - faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

#também posso usar from math import radians, sin, cos, tan e retirar o "math" das linhas

#=============================================================================================================================

#desafio 19 - o professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
#deles e escrevendo o nome do escolhido

import random  #posso usar -> from random import choice | e tirar o random da linha 86
primeiro = str(input('Primeiro aluno: '))
segundo = str(input('Segundo aluno: '))
terceiro = str(input('Terceiro aluno: '))
quarto = str(input('Quarto aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
escolhido = random.choice(lista)  #o random é quem seleciona o aleatório escolhido, choice vai ser a escolha de dentro da lista
print('O aluno escolhido foi {}'.format(escolhido))

#===================================================================================================================================


#desafio 20 - o professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro
#alunos e mostre a ordem sorteada

import random  #posso usar -> from random import shuffle e tirar o random da linha 101
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação desses alunos será: ')
print(lista)

#====================================================================================================================================

#desafio 21 - faça um programa em python que abra e reproduza o áudio de um arquivo MP3

#feito em um arquivo separado

#=====================================================================================================================================
