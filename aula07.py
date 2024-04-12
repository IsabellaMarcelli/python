#aula07

#n1 = int(input('Um valor: '))
#n2 = int(input('Outro valor: '))
#print('A soma vale {}'.format(n1+n2)) #poderia usar uma variável também, ex.: soma = n1 + n2

#num1 = int(input('Um valor: '))
#num2 = int(input('Outro valor: '))
#s = num1 + num2
#m = num1 * num2
#d = num1 / num2
#dint = num1 // num2
#e = num1 ** num2
#print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d)) #se quiser a divisão com 3 casas decimais eu faço: a divisão é {:.3f}
#print('Divisão inteira {} e potência {}'.format(dint, e))

#desafio 05 - faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor

n = int(input('Insira um número para saber o seu sucessor e antecessor: '))
suc = n + 1
ant = n - 1
print('O sucessor é {}'.format(suc))
print('O antecessor é {}'.format(ant))

#ou poderia fazer da seguinte forma:
#n = int(input("Digite um número: "))
#print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}".format(n, (n-1) , (n+1)))

print('========================================')

#desafio 06 - crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

valor = int(input('Insira um valor: '))
dobro = valor * 2
triplo = valor * 3
raiz = valor ** (1/2) #import math e depois math.sqrt pode ser usado para calcular a raiz quadrada também, ou então pow(n,(1/2))
print('O dobro é {}, o triplo é {} e a raíz quadrada é {}'.format(dobro, triplo, raiz)) #se quiser só 2 casas decimais na raiz quadrada eu uso {:.2f}
print('========================================')

#desafio 07 - desenvolva um programa que leia duas notas, calcule e mostre a sua média 

nota1 = float(input('Coloque a primeira nota: '))
nota2 = float(input('Coloque a segunda: '))
media = (nota1 + nota2) / 2
print('A média entra {} e {} é {}'.format(nota1, nota2, media)) #se eu quiser apenas um digito com ponto flutuante eu uso {.:1f}
print('========================================')

#desafio 08 - escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valorM = float(input('Insira um valor em metros: '))
cent = valorM * 100
milim = valorM * 1000
print('Esse valor em centímetros é {} e em milímetros é {}'.format(cent, milim))
print('=' * 40) #fazer a conversão pra km, hectometros, decametros e decimetros 

#desafio 09 - faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

numT = int(input('Insira um número para saber a sua tabuada: '))
print('{} x {:2} = {}'.format(numT, 1, numT*1))  #:2 só pra vizualizar melhor 
print('{} x {:2} = {}'.format(numT, 2, numT*2))
print('{} x {:2} = {}'.format(numT, 3, numT*3))
print('{} x {:2} = {}'.format(numT, 4, numT*4))
print('{} x {:2} = {}'.format(numT, 5, numT*5))
print('{} x {:2} = {}'.format(numT, 6, numT*6))
print('{} x {:2} = {}'.format(numT, 7, numT*7))
print('{} x {:2} = {}'.format(numT, 8, numT*8))
print('{} x {:2} = {}'.format(numT, 9, numT*9))
print('{} x {:2} = {}'.format(numT, 10, numT*10))
print('-' * 12)


#desafio 10 - crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#US$1,00 = R$3,27
real = float(input('Quanto dinheiro você tem na carteira? R$ '))
#cotação do dólar = 3,27
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('=' * 40)

#desafio 11 - faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2metros quadrados 
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura  
tinta = area/2
print('Sua parede tem dimensão de {} x {} e sua área é de {} m²'.format(largura, altura, area))
print('Essa parede de {} metros precisará de {} litros de tinta'.format(area, tinta))
print('=' * 40)

#desafio 12 - faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto = float(input("Insira o valor do produto: "))
produto_com_desconto = produto - (produto * 0.05)
print("O valor desse produto com o desconto de 5% é de {:.2f}".format(produto_com_desconto))
print('=' * 40)

#desafio 13 - faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input("Insira o salário do funcionário: "))
aumento = salario * 0.15
novo_salario = salario + aumento 
print('O salário do funcionário era de R$ {:.2f}, depois dos 15% de aumento o novo salário é de R$ {:.2f}'.format(salario, novo_salario))
print('=' * 40)

#outra forma de fazer é:
#salario = float(input('Qual é o salário do funcionário? R$'))
#novo = salario + (salario * 15/100)
#print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))

#desafio 14 - escreva um programa que converta uma temperatura digitada em ºC e converta para ºF
celsius = float(input('Insira uma temperatura em ºC: '))
f = ((9 * celsius) / 5) + 32
print('A temperatura {} em ºC convertida pra ºF é {}'.format(celsius, f))

#desafio 15 - escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele
#foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
km = float(input("Quantos KM foram percorridos pelo carro? "))
dias = int(input("Você alugou esse carro por quantos dias? "))
km_rodado = km * 0.15
dia_aluguel = dias * 60
total = km_rodado + dia_aluguel
print("O preço a pagar pelo carro que rodou {} km/h durante {} dias é de R${}".format(km, dias, total))