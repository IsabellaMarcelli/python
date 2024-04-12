#aula 12

nome = str(input('Qual é seu nome? '))
if nome == 'Isabella':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Pamela':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('Belo nome feminino!')
print('Tenha um bom dia, {}'.format(nome))

print('===============================================================')

#desafios

#desafio 36 - escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, 
#o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela (parcela) não pode exceder 30% do  
#salário ou então o empréstimo será negado. 

valor = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento?'))
prestacao = valor / (anos * 12) #anos * 12 pra saber em quantos meses ele vai pagar
minimo = salario * 0.3 #guanabara criou essa variável
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(valor, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestacao))

'''if prestacao < (salario * 0.3) + salario : 
    print('')'''

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo negado')

print('===============================================================')

#desafio 37 - escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexidecimal 

inteiro = int(input('Digiite um número inteiro de sua escolha: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))

if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(inteiro, bin(inteiro) [2:])) #pra ler a partir da terceira string e ir ate o fim
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(inteiro, oct(inteiro) [2:]))
else:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(inteiro, hex(inteiro) [2:]))

'''ou então pode usar mais um elif no lugar do else:
elif:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(inteiro, hex(inteiro)))
else:
    print('Opção inválida, tente novamente!')'''

print('===============================================================')

#desafio 38 - escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# "o primeiro valor é maior" ou "o segundo valor é maior" ou "não existe valor maior, os dois são iguais"

num1 = int(input('Insira um numero inteiro: '))
num2 = int(input('Insira um segundo: '))

if num1 > num2:
    print('{} é maior do que {}'.format(num1, num2))
elif num2 > num1:
    print('{} é maior do que {}'.format(num2, num1))
else:
    print('{} é IGUAL a {}'.format(num1, num2))

#desafio 39 - faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# - se ele ainda vai se alistar ao serviço militar, - se é a hora de se alistar, - se já passou do tempo de alistamento 
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo 

from datetime import date
atual = date.today().year 

nasc = int(input('Em que ano esse candidato nasceu?'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))

elif idade > 18:  #poderia ter usado apenas -> else:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo 
    print('Seu alistamento foi em {}'.format(ano))

#desafio 40 - crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com 
#a média atingida: - média abaixo de 5.0: reprovado, - media entre 5.0 e 6.9: recuperação, - média 7.0 ou superior: aprovado 

nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda: '))

media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, media))

if media < 5.0 :
    print('Esse aluno está REPROVADO !')

elif (media >= 5.0) and (media < 7.0):  #ou posso escrever  if 7 > media >= 5: 
    print('Esse aluno está de RECUPERAÇÃO !')

else:
    print('PARABÉNS! Você está APROVADO!')


#desafio 41 - a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
#de acordo com a idade: - até 9 anos: mirim, - até 14 anos: infantil, até 19 anos: junior, - até 25 anos: sênior, - acima: master 

from datetime import date 

atual = date.today().year
nascimento = int(input('Em que ano este atleta nasceu? '))
idade = atual - nascimento
print('Esse atleta tem {} anos'.format(idade))

if idade <= 9:  
    print('Esse atleta se classifica como atleta MIRIM')

elif (idade > 9) and (idade <= 14): #ou apenas:  elif idade <= 14:
    print('Esse atleta se classifica como atleta INFANTIL') 

elif(idade > 14) and (idade < 20):   #ou apenas:  elif idade <= 19:
    print('Esse atleta se classifica como atleta JÚNIOR')

elif (idade > 14) and (idade <= 25):   #ou apenas: elif idade <= 25:
    print('Esse atleta se classifica como atleta SÊNIOR')

else:   #elif (idade > 20):
    print('Esse atleta é classificado como atleta MASTER')


#desafio 42 - refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - equilátero, isósceles ou escaleno 
    
l1 = float(input('Insira o valor do 1º lado do triângulo: '))
l2 = float(input('Insira o valor do 2º lado do triângulo: '))
l3 = float(input('Insira o valor do 3º lado do triângulo: '))

if (l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2):
    print('As medidas fornecidas formarão um triângulo!' , end= '')

    if (l1 == l2) and (l2 == l3): # posso colocar l1 == l2 == l3
        print(' - EQUILÁTERO')
    
    elif (l1 == l2) or (l2 == l3) or (l3 == l1):
        print(' - ISÓSCELES')
    
    else:  #posso colocar l1 != l2 != l3   , posso colocar -> elif (l1 != l2) and (l2 != l3) and (l3 != l1):
        print(' - ESCALENO')

else:
    print('O triângulo NÃO poderá ser formado!') 


#desafio 43 - desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo
# abaixo de 18.5: abaixo do peso, entre 18.5 e 25: peso ideal, 25 até 30: sobrepeso, 30 até 40: obesidade, acima de 40: obesidade mórbida
    
print('=== CALCULANDO IMC ===')
peso = float(input('Insira o peso da pessoa: (kg) '))
altura = float(input('Insira a altura: (m) '))
imc = peso / (altura**2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Essa pessoa está ABAIXO do peso')

elif imc >= 18.5 and imc < 25:                 #ou posso colocar -> elif 18.5 <= imc < 25: 
    print('PARABÉNS! Você está no peso IDEAL')

elif imc >= 25 and imc < 30:
    print('Essa pessoa está em SOBREPESO!')

elif imc >= 30 and imc <= 40:
    print('OBESIDADE!')

elif imc > 40:
    print('OBESIDADE MÓRBIDA!')

#desafio 44 - elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - a vista dinheiro/cheque: 10% de desconto  - a vista no cartão: 5% de desconto  - em até 2x no cartão: preço normal 
# - 3x ou mais no cartão: 20% de juros 
    
print('{:=^40}'.format(' LOJA DA MARCELLI '))  # {:^40} = o nome centralizado em 40 espaços com o símbolo "="
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Qual a opção escolhida? '))

if opcao == 1:
    total = preco - (preco * 10 / 100) 
elif opcao == 2:
    total = preco - (preco * 0.05)

elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))

elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcelas = total / totparc
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(totparc, parcelas))
else:   #usei o else pra opção 5, que na verdade não existe 
    total = preco
    print('OPÇÃO INVÁLIDA DE PAGAMENTO, TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))

#desafio 45 - crie um programa que faça o computador jogar Jokenpô com você 

from random import randint
from time import sleep 
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: #computador jogou pedra 
    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR VENCE')

    elif jogador == 2:
        print('COMPUTADOR VENCE')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:  #computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')

    elif jogador == 1:
        print("EMPATE")

    elif jogador == 2:
        print('JOGADOR VENCE')

    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:  #computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')

    elif jogador == 1:
        print('COMPUTADOR VENCE')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('JOGADA INVÁLIDA') 