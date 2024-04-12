import moeda  

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')   # 1º moeda: nome do módulo , 2º moeda: nome da função
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')  # pegando o dobro do preço e convertendo pra um formato de moeda
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')  


