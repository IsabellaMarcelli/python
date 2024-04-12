'''def lin():
    print('-' * 30)


# Programa principal
lin()  # sempre que eu chamar o lin ele vai fazer a linha , se eu tirar o comando lin lá de cima ele da erro 
print('   ISABELLA   ')
print('   OLIVEIRA   ')
print('   MARCELLI   ')
lin()'''

def título(txt):  # título é o nome da função
    print('-' * 30)
    print(txt)  # vai ser substituido por curso em vídeo
    print('-' * 30)

# programa principal
título('   CURSO EM VÍDEO   ')

def soma(a, b):
    s = a + b
    print(s)

# programa principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
#soma(4)  # vai dar erro porque na função eu passei dois parâmetros e não 1
soma(a=4, b=5)

# ===================

def soma(c, d):
    print(f'C = {c} e D = {d}')
    s = c + d
    print(f'A soma C + D = {s}')

soma(4, 5) # ou (c=4, d=5)
#soma(7, 2)  # o 7 e o 2 substitui o lugar de 4 e 5 e faz a soma
#soma(3, 9, 5)  não funciona porque soma recebe apenas dois valores e não três 

# ==================

def contador(* núm):  # significa que vou receber parâmetros mas não sei quantos
    for valor in núm:
        print(f'{valor} ', end='')   # end é pra não quebrar a linha
    print('FIM!')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

''' def contador(* núm):  
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')  # função padrão que vai mostrar os números na tela e também contar 

contador(4, 8, 6)
contador(7, 1)
contador(24, 9, 11, 3) ''' 

# outro exemplo de desempacotamento:
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)

# ==== EXEMPLOS COM LISTA ====

def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2  # vai receber o dobro
        pos += 1  # aqui ele avança pro próximo índice da lista

valores = [6, 3, 9, 1, 3]   # isso não é desempacotamento, é diferente de tuplas
dobra(valores)  # passei como parâmetro 'valores' então ele vai criar uma lista 'valores' e vai passar pa 'lst' e nesse momento vou ter duas listas na memória (valores e lst) , tudo o que eu fizer em 'lst' vai interferir em 'valores'
print(valores)

# desafio 96 - faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno 
# retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área desse terreno é de {a} m²')  # poderia escrever {largura} * {comprimento} = {a}

# programa principal
l = float(input('Insira a largura do terreno (m): '))
c = float(input('Insira o comprimento (cm):  '))
area(l, c)

# desafio 97 - faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável. Ex.: escreva('Olá, Mundo!')   
# saída:
# -------
# Olá, Mundo!
# -------

def escreva (msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

# programa principal

escreva('Oi')   # o nome definido aqui tem que ser o mesmo da função 
escreva('Isabella')
escreva('Sou eu')

'''entrada = input('Escreva algo: ')
escreva(entrada)'''

# desafio 98 - faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e 
# passo e realize a contagem.  Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1    b) De 10 até 0, de 2 em 2  c) Uma contagem personalizada.

from time import sleep
def contador(inic, fim, passo):
    
    if passo < 0:  # se o passo for negativo... faça
        passo *= -1   # multiplicando por -1 e tornando esse passo positivo, não vai dar errado porque você vai estabelecer o fim 
    if passo == 0:  # passo 0 não existe, se fosse 0 não iria dar passo e sim ficar parado
        passo = 1

    print('*' * 30)
    print(f'Contagem de {inic} até o {fim} de {passo} em {passo}')
    sleep(1.0)

   
    if inic < fim:
        cont = inic
        while cont <= fim:   # isso só serve se o início for menor que o fim, por isso fiz o IF
            print(f'{cont} ', end='', flush=True)
            sleep(0.4)
            cont += passo
        print('FIM!')
    else: 
        cont = inic
        while cont >= fim:  # porque o fim é maior
            print(f'{cont} ', end='', flush=True) # não vai ligar o bufer de tela, pro sleep funcionar
            sleep(0.5)
            cont -= passo
        print('FIM!')

# programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('*' * 30)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(inicio, f, p)

# desafio 99 - faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores 
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):   # quero desempacotar usando uma estrutura de repetição, que é o for 
    cont = maior = 0
    print('-*' * 20)
    print('Analisando os valores passados...')
    for valor in num: 
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:   # ou seja, se eu não tenho número nenhum ainda...
            maior = valor 
        else: 
            if valor > maior:
                maior = valor 
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')


# programa principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# desafio 100 - faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma 
# entre todos os valores PARES sorteados pela função anterior.

from random import randint

def sorteia(lista): # vai receber uma lista
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5): # vai ignorar o último
        lista.append(randint(1, 10))  #vai sortear um número entre 1 e 10
        

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor 
    print(f'Somando os valores pares da lista {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
print(numeros)
somaPar(numeros)

# aula 20 - parte 2

'''print(input.__doc__)
help(input)'''

def somar( a=0, b=0, c=0):
   
    s = a + b + c
    print(f'A soma vale {s}', end='')  # o end é um parâmetro opcional

#somar(3, 3)
somar(b=4, c=2)  # ou c=3, a=2
somar()   # vai dar 0

# =============== escopo de variáveis ===================

def funçao():
    n1 = 4  # variável local
    print(f'N1 dentro vale {n1}')

n1 = 2  # variável global
funçao()
print(f'N1 fora vale {n1}')




def teste(b):
    global a 
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5  # A aqui passa a valer 8 também
teste(a)
print(f'A fora vale {a}')

# ========== funções com retorno ==========

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2}, {r3}')

# ====== exercício na prática ======

def fatorial(num=1):   # numero vai ser 1 caso eu não informe
    f = 1
    for c in range(num, 0, -1):
        f *= c  # f = f * c
    return f  # não é apenas pra número, pode ser algum valor lógico por exemplo

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

# também posso fazer: 
'''f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')'''

# ====== valor verdadeiro ou falso ======

def par(n=0):
    if n%2 == 0:
        return True  # vai ser par
    else:
        return False  # vai ser ímpar
    
num = int(input('Digite um número: '))
if par(num):    # se for par... (porque )
    print('É par!')
else:
    print('Não é par!')

# =========== desafios ==============
    
# desafio 101 - crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de 
# nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL 
# ou OBRIGATÓRIO nas eleições.

#from datetime import date  # tirei essa linha daqui e coloquei dentro da def pra usar APENAS dentro da def (isso economiza mem´roa)
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16: 
        return f'Com {idade} anos NÃO VOTA.'
    elif idade > 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é OPCIONAL!'
    else:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'

nasc = int(input('Em que ano você nasceu? '))  # acrescentei essa linha
print(voto(nasc))  # aqui antes de nasc estava um ano aleatório que eu escolhi

# desafio 102 - crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial.

def fatorial(n, show=False):  # false porque é opcional
    f = 1
    for c in range(n, 0, -1):
        if show: 
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f*= c
    return f

# programa principal
print(fatorial(5, show=True))  # quando coloco True ele mostra
# help(fatorial)   # mas o help não está funcionando

# ========================================================================
    
# desafio 103 - faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome
# de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que 
# algum dado não tenha sido informado corretamente.

def ficha(jog='<desconhecido>', g=0): # porque ambos são opcionais
    print('-' * 20)
    print(f'O jogador {jog} fez {g} gol(s)')

nome = str(input('Nome do jogador: '))
gols = (str(input('Quantos gols ele fez? ')))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':    # ou seja, se eu tirei todos os espaços e o nome ficou vazio = não escrevi nada
    ficha(g=gols)   # só coloquei gols pq aqui no caso nome vai ser vazio

else:
    ficha(nome, gols) 

# desafio 104 - crie um programa que tenha a funçao leiaInt(), que vai funcionar de forma semelhante à função input()
# do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex.: n = leiaInt('Digite um n')
    
def leiaInt(msg):
    ok = False
    valor = 0
    while True: 
        n = str(input(msg))
        if n.isnumeric():  #se o valor for numérico ele vai receber um inteiro
            valor = int(n)
            ok = True  # e o ok fica tru
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido: \033[m')
        if ok: 
            break
    return valor

# programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
    
# desafio 105 - faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações: 
# - quantidade de notas
# - a maior nota
# - a menor nota
# - a média da turma
# - a situação (opcional)
# adicione também as docstrings da função.

def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)

    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'

        elif r['média'] >=5:
            r['situação'] = 'RAZOÁVEL'

        elif r['média'] < 5:
            r['situação'] = 'RUIM'
    return r

#programa principal
resp = notas( 5.5, 2.5, 1.5, sit=True)  # se colocar só true não
print(resp)
#help(notas)        - não deu pra fazer as docstrings
    
# desafio 106 - faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando 
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Obs.: use cores

from time import sleep
# variável global: 
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m'   # 1 - vermelho 
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30'       # 6 - branco
     );

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# programa principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':   #posso escrever fim maiúsculo, minúsculo ou misturado...
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
