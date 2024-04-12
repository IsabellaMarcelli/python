#cadeia de caracteres / Manipulando texto / aula 09

frase = 'Curso em Vídeo Python'
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python' , 'Android'))
print(frase[0]) #vai imprimir C, que é a primeira letra
#mas não posso fazer a posição 0 receber J, ex.: frase[0] = 'J' , porque uma string é imutável
print('=========================================')

frase2 = 'Isabella gosta de treinar'
frase.replace('treinar', 'comer') #pra imprimir isso aqui alterado / com a substituição 
#eu devo fazer: frase = frase.replace('treinar', 'comer') , veja:
frase2 = frase2.replace('treinar' , 'comer')
print(frase2)
print(frase2.find('gosta'))

print('========================================================')

#pra colocar tudo em print eu uso 3 aspas duplas antes e 3 aspas duplas depois dos parenteses

print("""Meu nome é Afonso Soares de Melo, e resolvi contar algo que se passou comigo: 
Estava sentado no meu escritório quando lembrei de uma chamada telefônica que tinha que fazer. 
Encontrei o número e disquei. Atendeu-me um cara mal humorado dizendo:
Fale!!!
Bom dia. Poderia falar com Andréa? O cara do outro lado resmungou algo que não entendi e 
desligou na minha cara""")

print('========================================================================================')

frase3 = 'Olha como vem'
dividido = frase3.split()
print(dividido[2])

print('=======================')

#desafio 22 - crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas
# - O nome com  todas minúsculas  - Quantas letras ao todo (sem considerar espaços)  - Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: ")).strip() #strip usado pra ignorar os espaços que vem antes e depois do nome 
print("Analisando seu nome...")
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #quantidade de letras menos o contador de espaços
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))  #usa o comando pra encontrar o primeiro espaço e fazer a contagem do 1º nome

#ou posso fazer da seguinte forma:

separa = nome.split()  #split vai jogar dentro de uma lista de nomes inteiros 
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

print('================================================================================================')


#desafio 23 - faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados (unidade, dezena, centena, milhar)

num = int(input('Informe um número: '))
u = num // 1 % 10 # usei // porque eu quero a divisão inteira
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

print('===========================================')


#desafio 24 - crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

cid = str(input('Em que cidade você nasceu? ')).strip() #strip pra retirar os espaços 
print(cid[:5].upper() == 'SANTO')  #o comando joga a primeira palavra tudo pra maiúscula pra verificar se tem santo no nome ou não 

print('===========================================================')

#desafio 25 - crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome 

nome_pessoa = str(input('Qual é o seu nome completo? '))
print('Seu nome tem Silva? {}'.format('silva' in nome_pessoa.lower()))

print('===================================================')

#desafio 26 - faça um programa que leia uma frase pelo teclado e mostre: - Quantas vezes aparece a letra "A"    
# - Em que posição ela aparece a primeira vez     - Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).upper().strip()  #upper joga a frase toda pra maiúscula pra verificar e strip tira os espaços
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1)) #coloquei +1 porque começa contando no 0
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1)) #vai localizar a partir do lado direito, do fim pro começo

print('===============================================================')

#desafio 27 - faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

n = str(input('Digite seu nome completo: ')).strip()
nome_da_pessoa = n.split() #split divide o nome em pedaços, formando uma lista
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome_da_pessoa[0]))
print('Seu último nome é {}'.format(nome_da_pessoa[len(nome_da_pessoa)-1]))   #len nome pra saber quantas posições tem o nome 

#fiquei com um pouco de dúvida 

print('==================================================')



