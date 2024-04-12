lanche = ('Sorvete' , 'Pizza', 'Torta', 'Sushi')
print(lanche[1:3])  #desconsidera o último
print(lanche[2:])  #2 até o final
print(lanche[:2])  #do inicio até o 2 - ele sempre ignora o 2 
print(lanche[-3:])   #menos 3 até o final (pizza, torta e sushi)

#tuplas são IMUTÁVEIS 

for comida in lanche:
    print(f'Eu vou comer {comida}')

#quando o programa tiver parado eu posso mexer na tupla, só não posso mexer quando ele tiver em execução

for cont in range(0, len(lanche)):      #no range ele também ignora o último item
    #print(cont)                              #range começa em 0, depois vai pra 1, 2... vai de 0 a 3  / cont vai de 0 a 3
    print(f'Eu vou comer {lanche[cont]}')


print('Comi pra caramba!')



a = (2, 4, 8)
b = (1, 7, 10)
c = a + b
print(c)

#===============================================================================================================================================

# desafio 72 - crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte. Seu programa 
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'O número digitado foi {cont[num]}')

#desafio final ainda precisa ser feito 

#==========================================================================================================================

#desafio 73 - crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
#depois mostre:   A) Apenas os 5 primeiros colocados.   B) Os últimos 4 colocados na tabela.   C) Uma lista com os times em ordem alfabética
#  D) Em que posição na tabela está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 
         'Cruzeiro' , 'Flamengo' , 'Vasco', 'Chapecoense', 
         'Atletico', 'Botafogo', 'Atlético - PR', 'Bahia',
            'São Paulo', 'Fluminense' , 'Sport Recife',
           'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 
            'Atlético - GO')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times} ')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos times são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
#print(f'O time do Chapecoense está na {times.index("Chapecoense") + 1} posição')  - nao deu certo

#desafio 74 - crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números
#gerados e também indique o menor e o maior valor que estão na tupla

from random import randint
numeros = (randint (1, 10), randint (1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

'''print(f'Eu sorteei os valores {n}')'''              #posso fazer desse jeito também 

print('Os valores sorteados foram: ', end = '')          
for n in numeros:
    print(f'{n} ', end = ' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

#desafio 75 - desenvolva um programa que leia quatro valores pelo teclado e guarde - os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9      B) Em que posição foi digitado o primeiro valor 3     C) Quais foram os números pares. 

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end='')
for n in num:                 #só vai mostrar SE o número for divisivel por 2
    if n % 2 == 0:
        print(n, end = ' ')

#desafio 76 - crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre 
#uma listagem de preços, organizando os dados em forma tabular.
        
listagem = ('Lápis', 1.75, 
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos] :.<30}', end = '')
    else:
        print(f'R$ {listagem [pos]:>7.2f}')
print('-' * 40)

#desafio 77 - crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra,
#quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end = ' ')
    for letra in p:
        if letra.lower() in 'aeiou':          #com acento eu teria que colocar as letras com acento
            print(letra, end = ' ')

