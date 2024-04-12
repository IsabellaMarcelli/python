import moeda     # quero manter a formatação de 2 casas decimais, mas sem moeda.moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')   
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')  
print(f'Aumentando em 10%, temos {moeda.aumentar(p, 10, False)}')  # não vai estar formatado 
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
