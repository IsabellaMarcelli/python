nome = 'jose'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e recebe {salario:.2f} por mês')

#desafio 66 - crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que 
#é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = cont = 0
soma = 0
while True:
    n = int(input('Insira um número: (999 para parar) '))
    if n == 999:
        break
    cont += 1  #coloquei aqui porque o flag não vai ser considerado 
    soma += n
print(f'O total de números foi {cont} e a soma dos valores fornecidos é {soma}')

#desafio 67 - faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será
#interrompido quando o número solicitado for negativo. 

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-'*30)

    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')

    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO!')

#desafio 68 - faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total 
#de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True: 
    print('=-'*14)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-'*14)
    num = int(input('Digite um valor: '))
    computador = randint(0, 11)
    total = num + computador
    escolha = ' '
    while escolha not in 'PI':  #enquanto escolha não for 'PI' ...    #não coloquei os minúsculos pq usei upper na linha de baixo
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper() [0]  # 0 é a primeira letra
    print(f'Você jogou {num} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('Você GANHOU!')
            v += 1  #contador 'vitoria' conta quantas vezes o jogador ganhou
            
        else:
            print('Você PERDEU!')
            break    #pra parar o laço

    elif escolha == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')   #só vai jogar de novo se o jogador ganhar

print(f'GAME OVER!! Você venceu {v} vezes.')  #só exibe essa mensagem se o jogador perder, se ele ganhar o looping se repete e jogam de novo

#desafio 69 - crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
#quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados
# C) Quantas mulheres tem menos de 20 anos.

cont = 0
contmasc = 0
contfem = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '  #string vazia pra definir o sexo
    while sexo not in 'MF':   #enquanto não decidir entre masc ou fem ele não vai deixar passar
        sexo = str(input('Sexo: [M/F] ')).strip().upper() [0]
        if idade > 18:
            cont += 1

 
        if sexo == 'M':
            contmasc += 1


        elif sexo == 'F': 
            if idade < 20:
                contfem += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper() [0]
    if resp == 'N':
        break

print(f'{cont} pessoas tem mais de 18 anos, {contmasc} homens foram cadastrados e {contfem} mulheres tem menos de 20 anos.')


#desafio 70 - crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final,
#mostre:  A) Qual é o total gasto na compra.     B) Quantos produtos custam mais de R$1000.      C) Qual é o nome do produto mais barato

tot = cont = menor = contprod = 0   #contprod pra contar quantos produtos eu tenho e saber se o primeiro é o mais caro ou o segundo
barato = ' '
while True:
    produto = ' '
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    contprod += 1  #assim que eu li o produto e o preço eu tenho um novo produto 
    tot += preco

    if preco > 1000:
        cont += 1

    if contprod == 1 or preco < menor: #se for o primeiro produto o mais barato
      
        menor = preco
        barato = produto
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper() [0]

    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra foi {tot:.2f}, {cont} produtos custam mais de R$ 1000 e o produto mais barato é o {barato}')

#desafio 71 - crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.  Obs.: considere que o caixa possui cédulas de 
# R$50, R$20, R$10 e R$1.  

print('=' * 30)
print('{:^30}'.format('BANCO MARCELLI'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO MARCELLI! Tenha um bom dia!')

