'''for c in range (1, 10):
    print(c)
print('Fim')'''

'''c = 1 #contador começa com 1
while c < 10:  #enquanto o contador não chegar a 10 / for menor do que 10:
    print(c)
    c = c + 1
print('Fim')'''

'''n = 1
while n != 0:   #condição de parada
    n = int(input('Digite um valor: '))
print('Fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))

#desafio 57 - faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
#novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper() [0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper() [0]
print('Sexo {} registrado com sucesso'.format(sexo))

#desafio 58 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar adivinhar até
#acertar, mostrando no final quantos palpites foram necessários para vencer. 

from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador: 
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print('Acertou com {} palpites.'.format(palpites))

#desafio 59 - crie um programa que leia DOIS VALORES e mostre um MENU na tela:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVOS NÚMEROS 
# [5] SAIR DO PROGRAMA
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
opcao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>> Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre os dois números é {}'.format(soma))
    
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre os dois valores é {}'.format(mult))
    
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior do que {}'.format(n1, n2))
        
        else:
            print('O número {} é maior do que {}'.format(n2, n1))

    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Saindo...')

    else: 
        print('Opção inválida. Tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa!')

#desafio 60 - Faça um programa que leia um número qualquer e mostre o seu fatorial, ex.: 5! = 5x4x3x2x1 = 120 (fazer com enquanto e for)

from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))

print('===================================')

n = int(input('Digite um número para calcular seu fatorial: '))
c = n 
f = 1 #já que meu fator nulo de MULTIPLICAÇÃO é 1, 9*1 = 9, 6*1 = 6...
print('Calculando {}! = '.format(n) , end= '')
while c > 0:
    print('{}'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c    # f = f * c
    c -= 1
print('{}'.format(f))

print('====================================')

#utilizando FOR:

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando...{n} : ', end = '')
for fatorial in range (n, 0, -1):
    print(f'{c}', end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    c -= 1
    f *= fatorial
print(f'{f}')

#desafio 61 - Refaça o desafio 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 primeiros termos da progressão usando a 
#estrutura while 

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1   #aqui vai contar quantos termos foram, até o 10 que coloquei no while 
while cont <= 10:
    print('{} -> '.format(termo), end = '')
    termo += razao
    cont += 1
print('FIM')

#desafio 62 - Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser
#que quer mostrar 0 TERMOS.

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1   #aqui vai contar quantos termos foram, até o 10 que coloquei no while 
total = 0
mais = 10  #programa já começa mostrando 10 termos 
while mais != 0: 
    total = total + mais 
    while cont <= total:
        print('{} -> '.format(termo), end = '')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))

#desafio 63 - Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma SEQUÊNCIA DE 
#FIBONACCI. Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end = '')
cont = 3 #em 3 pq ja mostrei o primeiro e o segundo termo
while cont <= n: 
    t3 = t1 + t2
    print(' -> {}'.format(t3), end = '')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*30)

#desafio 64 - crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor "999",
#que é a condição de parada. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles (desconsiderando o flag - 999).

n = 0
soma = 0
cont = 0
n = int(input('Insira um número [999 pra parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Insira um número [999 pra parar]: '))
print('Foram digitados {} números e a soma foi {}'.format(cont, soma))  

#leio o flag dentro e fora porque se o número for 999 ele termina e não volta pro while novamente, já que while num != 999

''' poderia fazer:

n = cont = soma = 0

while n != 999:
    n = int(input('Insira um número [999 pra parar]: '))
    cont += 1
    soma += n
print('Foram digitados {} números e a soma foi {}'.format(cont - 1, soma - 999)) #mas aqui você só ta eliminando 999 da conta ''' 

#desafio 65 - crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual
#foi o MAIOR e MENOR valores lidos. O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar valores.

resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Ss':   #enquanto minha resposta estiver em sim maiúsculo ou minúsculo 
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num 
        
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip() [0]
media = soma/quant
print('Você digitou {} valores e a média foi {:.2f}'.format(quant, media))
print('O maior valor digitado foi {} e o menor é o {}'.format(maior, menor))



 