'''i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print (c)
print('FIM')'''

'''for c in range (0, 3):   #esse comando pra ler está dentro de um for, então isso acontece 3 vezes, ele printa a pergunta 3 vezes
    n = int(input('Digite um valor: '))
print('fim')'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n   # = s = s + n
print('O somatório de todos os valores foi {}'.format(s))

#desafios

#desafio 46 - faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma 
#pausa de 1 segundo entre eles.

from time import sleep
for c in range (10, -1, -1):
    print(c)
    sleep(0.5)
print('POW! POW! BUMMM!')

#desafio 47 - crie um programa que mostre na tela todos os números PARES que estão no intervalo entre 1 e 50.

for cont in range (2, 51, 2):
    print(cont, end=' ')

#desafio 48 - faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo
#de 1 até 500
    
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
     cont += 1    #um contador normalmente soma 1  |  contador dentro do If porque só quero contar os que são multiplos de 3  |  cont += 1    =  cont = cont + 1
     soma += c    #um acumulador normalmente soma um valor ao outro  |  soma = soma + c  =  soma += c (soma recebe ele mesmo + c)
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

#desafio 49 - refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

num = int(input('Digite um número para ver sua tabuada: '))   #este código está dando erro 
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
    

#desafio 50 - desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado 
#for ímpar, desconsidere - o.
    
soma = 0
for c in range(1, 7):
    num = int(input('Insira um valor: '))

    if num % 2 == 0:
        soma += num
print('A soma dos números pares é igual a {}'.format(soma))

'''resolução do guanabara:
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))'''

#desafio 51 - desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão

print('====================')
print('10 TERMOS DE UMA PA')
print('====================')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao  #enézimo termo de uma PA
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end = ' -> ')
print('ACABOU')


#desafio 52 - faça um programa que leia um número inteiro e diga se ele é ou não um número primo. 

num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c ==0:
        print('\033[33m', end = '')
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{} '.format(c), end = '')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')


#desafio 53 - crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
    
    frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() 
junto = ''.join(palavras)
inverso = junto[::-1]
'''inverso = '''''

'''for letra in range(len(junto) -1, -1, -1): 
    inverso += junto[letra]'''
print(' O inverso de {} é {}'.format(junto, inverso))

if inverso == junto: 
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')

#desafio 54 - crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores. - maioridade: 21 anos
    
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input('Em que ano a {}º pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
        print('Essa pessoa é maior')
    else:
        totmenor += 1
        print('Essa pessoa é menor')
print('O total de pessoas menores de idade é {}'.format(totmenor))
print('O total de pessoas maiores de idade é {}'.format(totmaior))


#desafio 55 - faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}KG'.format(maior))
print('O menor peso lido foi de {}KG'.format(menor))

#desafio 56 - desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# -> a média de idade do grupo
# -> qual é o nome do homem mais velho 
# -> quantas mulheres tem menos de 20 anos

totid = 0
totmulher20 = 0
maioridadehomem = 0
nomevelho = ''
for info in range (1, 5):
    nome = str(input('Insira o nome da {}º pessoa: '.format(info)))
    sexo = str(input('Insira o sexo: [F/M] '))
    idade = int(input('Insira a idade: '))
    totid = totid + idade
    media = totid / 4

    if info == 1 and sexo in "Mm" :  #começo sempre analisando a primeira pessoa
       maioridadehomem = idade  #como não tenho ngm antes as duas variaveis recebem as informações da primeira pessoa 
       nomevelho = nome
    
    if sexo in 'Mm' and idade > maioridadehomem:
       maioridadehomem = idade
       maisvelho = nome

    if sexo in "Ff" and idade < 20:   #poderia ter escrito assim ->  if sexo == "F": , mas escrevi diferente pra pessoa poder inserir ou F ou f
        totmulher20 += 1

print('A média da idade de todos os membros do grupo é de {}'.format(media))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(maisvelho, maioridadehomem))
print('A quantidade de mulheres que tem -20 anos é de {}'.format(totmulher20))







