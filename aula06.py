#aula06

#OBS: input é sempre do tipo string, input faz referência a string / vou guardar uma string

nome = input("Digite o seu nome: ")
print("É um prazer te conhecer, " , nome)  #ou print('É um prazer te conhecer {}!'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
#print('A soma entre' , n1, 'e', n2, 'vale', s)
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))

n = float(input('Digite um valor: '))
print(n)   #vai imprimir o número informado com o ponto flutuante 

num = str(input('Digite outro valor: '))
print(type(num))

num1 = bool(input('Digite um valor: ')) 
print(num1)   #se eu inserir um valor ele imprime true, se eu só der enter e não colocar valor nenhum ele imprime falso 

num2 = input('Digite algo: ')
print(num2.isnumeric()) #se o que foi digitado for número ou puder ser convertido em número ou em um tipo primitivo int ele imprime true, se não ele imprime falso, ex.: "3a" não é numérico

num3 = input('Digite outra coisa: ') 
print(num3.isalpha()) #se o que for digitado fizer parte do alfabeto ele imprime true

num4 = input('Digite outro valor: ') 
print(num3.isalnum()) #aqui imprime true pra número junto com alfabeto, ex.: se eu der espaço ou enter ele imprime falso

#Desafios

#01:
valor1 = int(input('Insira um primeiro valor: '))
valor2 = int(input('Insira o segundo: '))
somando = valor1 + valor2
print('A soma entre ' , valor1, 'e', valor2, 'é igual a ', somando)

#02:
coisa = input('Digite algo: ')
print('O tipo primitivo desse valor é' , type(coisa))
print('Só tem espaços? ' , coisa.isspace())
print('É um número? ' , coisa.isnumeric())
print('É alfabético? ' , coisa.isalpha())
print('É alfanumérico? ' , coisa.isalnum())
print('Está em maiúsculas? ' , coisa.isupper())
print('Está em minúsculas? ' , coisa.islower())
print('Está capitalizada? ' , coisa.istitle())






      




