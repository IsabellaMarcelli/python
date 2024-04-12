pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
#pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
#del pessoas ['sexo']
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')   # já que na linha de cima coloquei aspas simples aqui no print coloco aspas duplas
for k, v in pessoas.items():
    print(f'{k} = {v}')

# criar um dicionário dentro de uma lista:
    
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

#print(brasil)  # mostra os dois dicionários
#print(brasil[0]) # o estado que foi add primeiro, que é RJ
print(brasil[0]['uf']) # corresponde a rio de janeiro
print(brasil[1]['sigla'])  # corresponde a SP

# ==========================================================

estado = dict()   # dict é o dicionário
brasil = list() 
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)

for e in brasil:
    #print(e)       # imprimiu cada estado que é um dicionário      # esse for de fora é da lista
    for k, v in e.items():   # k = chave, v = valor dentro de dicionário 
        print(f'O campo {k} tem valor {v}')

# ============================================================
        
# desafio 90 - faça um programa que leia nome e média de um aluno , guardando também a situação em um dicionário.
# no final mostre o conteúdo da estrutura na tela

aluno = dict()
aluno['nome'] = str(input("Nome: "))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 16)
for k, v in aluno.items():              # k: chave, v: valor ; items é o conjunto chave e valor
    print(f'{k} é igual a {v}') 
        
# desafio 91 - crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses 
# resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior 
# número do dado.
    
from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1, 6),
         'jogador2': randint(1, 6),
         'jogador3': randint(1, 6),
         'jogador4': randint(1, 6)}

# pra colocar em ordem vou criar o dicionário chamado ranking
ranking = list()   # vou usar lista / tuplas dentro da lista , por isso lá embaixo usei enumerate(ranking)

print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse =True)   # é recomendado criar outro dicionário pra ele poder ordenar ; 
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')                    # se for itemgetter(0) ele vai colocar em ordem o jogador, pra colocar o valor em ordem uso itemgetter(1)
                                                        # pra colocar o vencedor em primeiro eu uso reverse

for i, v in enumerate(ranking):
    print(f'   {i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
        
# desafio 92 - crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre - os (com idade)
# em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e
# o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
    
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados ['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
        
# desafio 93 - crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome
# do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
    
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
total_part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))  # não vou salvar dentro de dicionário pq só pediu nome, cada gol de cada partida e total, por isso criei a variável normal
for c in range(0, total_part):
    partidas.append(int(input(f'Quantos gols ele fez na {c+1}ª partida? ')))
jogador['gols'] = partidas[:]            # uma nova chave (gols) recebe uma cópia de partidas
jogador['total'] = sum(partidas)     #uma nova chave vai receber a soma das partidas, que no caso são os gols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f' {k} é igual a {v} ')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):    # aqui não coloco aspas duplas porque não está dentro de um print
    print(f'     => Na partida {i+1} fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols. ')
        
# desafio 94 - crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:  A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo    C) Uma lista com todas as mulheres    D) Uma lista com todas as pessoas com 
# idade acima da média 

galera = list()  # lista que vai receber o dicionário
pessoa = dict()
soma = 0
media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper() [0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))   # preencheu o dicionário com nome, sexo e função, mas agora preciso jogar dentro de uma lista
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper() [0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)   # a partir daqui eu to analisando os dados e mostrando os resultados
print(f'A) Ao todo {len(galera)} pessoas foram cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')  # 5 casas ao todo e 2 decimais
print('C) As mulheres cadastradas foram ', end='')
for p in galera:   # pra cada pessoa dentro de galera ....
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')

print('\nD) Lista das pessoas que estão acima da média: ', end='')
for p in galera: 
    if p['idade'] >= media:    # aqui ele fez meio diferente 
       print(f'{p["nome"]} ', end='') 
        
# desafio 95 - aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de 
# vizualização de detalhes do aproveitamento de cada jogador. 
       
time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()   # vou limpar pq sempre vou receber dados de um novo jogador 
    jogador['nome'] = str(input('Nome do Jogador: '))
    total_part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))  
    partidas.clear()

    for c in range(0, total_part):
        partidas.append(int(input(f'Quantos gols ele fez na {c+1}ª partida? ')))
    jogador['gols'] = partidas[:]            
    jogador['total'] = sum(partidas)    
    time.append(jogador.copy())
    while True: 
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N.')  # else...
    if resp == 'N':
        break

print('-=' * 24)    # a partir daqui tem os resultados
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}' , end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca] ["nome"]}: ')  # jogador está dentro de um time que tem um indice numérico (que é o indice da BUSCA) e dentro dele eu tenho o elemento nome que está dentro do funcionário
        for i, g in enumerate(time[busca] ['gols']):    # vai funcionar dentro da lista, por isso é um enumerate / g indica os gols (conteúdo dentro do índice)
            print(f'  No jogo {i+1} fez {g} gols. ')
    print('-' * 40)
print('<<< VOLTE SEMPRE! >>>')
       
       
