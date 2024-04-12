#exercícios aula 10 

nome = str(input("Qual é o seu nome? "))
if nome == 'Isabella':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}'.format(nome))

print('===============================')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda: '))
m = (n1 + n2) / 2 
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS! ')

print('============================================')

#desafio 28 - escreva um programa que faça o computador "pensar" em número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual 
#foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep #faz o computador esperar/dormir por alguns segundos 
computador = randint(0, 5)  # faz o computador "pensar" / sortear o número
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)
numero = int(input("Em que número eu pensei? ")) #jogador tenta adivinhar o número 
print('PROCESSANDO...')
sleep(1) #esperar 1 segundo pra imprimir o próximo print
if numero == computador: 
    print('PARABÉNS! Você acertou o número que eu estava pensando!')
else: 
    print('Você PERDEU! Eu pensei no número {} e não no {} KKKKKK'.format(computador, numero))

print('============================================')

#desafio 29 - escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi 
#multado. A multa vai custar R$ 7,00 por cada km acima do limite. 

velocidade = float(input('Qual a velocidade em que você está dirigindo?'))
if velocidade > 80: 
    print('VOCÊ ACABA DE SER MULTADO! - exceu o limite de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deverá pagar a multa no valor de R$ {:.2f} !'.format(multa))
print('Tenha um bom dia e dirija com segurança!')  #poderia colocar um else, mas estamos fzd exercício de condicional/condição simples

print('============================================')

#desafio 30 - crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR 

numInteiro = int(input('Insira um número qualquer: '))
if numInteiro % 2 == 0:
    print('O número {} é par'.format(numInteiro))
else:
    print('O número {} é ímpar'.format(numInteiro))

print('============================================')

#desafio 31 - desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 por KM para
#viagens de até 200KM e R$0,45 para viagens mais longas 

distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar a sua viagem de {} Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
    print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))
else:
    preço = distância * 0.45
    print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))

#ou posso fazer também: 

'''distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar a sua viagem de {} Km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))'''

print('============================================')

#desafio 32 - faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO 

from datetime import date
ano = int(input("Gostaria de analisar qual ano? (bissexto) Insira o nº 0 para analisar o ano atual."))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

print('============================================')

#desafio 33 - faça um programa que leia três números e mostre qual é o maior e qual é o menor. 

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

if v1 > v2 and v1 > v3 :
    print('O maior valor é o {}'.format(v1))

if v2 > v1 and v2 > v3:
    print('O maior valor é o {}'.format(v2))

if v3 > v1 and v3> v2:
    print('O maior valor é o {}'.format(v3))


if v1 < v2 and v1< v3:
    print('O menor valor é o {}'.format(v1))

if v2 < v3 and v2 < v1:
    print('O menor valor é o {}'.format(v2))

if v3 < v1 and v3 < v2:
    print('O menor valor é o {}'.format(v3))

#ou posso fazer da seguinte maneira:

'''a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando quem é menor 
menor = a 
if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c

#verificando quem é o maior 

maior = a
if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))'''

print('============================================')

#desafio 34 - escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a 
# R$1.250,00 , calcule um aumento de 10% .  Para os inferiores ou iguais o aumento é de 15% . 

salario = float(input('Qual o salário do funcionário? '))

if salario < 1250:
    aumento = (salario * 0.15) + salario
    print('O novo salário desse funcionário agora é {:.2f}'.format(aumento))

else:
    aumento = (salario * 0.10 #ou * 10 / 100) + salario
    print('O novo salário desse funcionário agora é de {:.2f}'.format(aumento))

#desafio 35 - desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo 

seg1 = float(input('Primeiro segmento de reta: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if (seg1 < seg2 + seg3) and (seg2 < seg1 + seg3) and (seg3 < seg2 + seg1):
    print('O triângulo poderá ser formado')

else:
    print('O triângulo NÃO poderá ser formado')

print('============================================')

#último desafio (cores): pegue uns 10 exercícios e coloque cores e nos 35 exercícios crie um sistema de cores pra eles 