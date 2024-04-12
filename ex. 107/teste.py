import moeda  # se eu quiser importar funções específicar eu escrevo from moeda import metade, dobro, aumentar , porque
#ai eu limito a quantidade de coisas carregadas, ou seja, carrego somente aquilo que é necessário

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é: R${moeda.metade(p)}')   # preciso passar um preço que vai ser meu parâmetro, que nesse caso é o p
print(f'O dobro de {p} é: R${moeda.dobro(p)}')
t = int(input('Digite um valor pra calcular a taxa: '))
print(f'Aumentando em {t}%, o {p} é: R${moeda.aumentar(p, t)}')  # a taxa é fixa, você altera somente no código 
#(mas depois fiz o t receber o input então o usuário pode digitar a taxa)
print(f'Diminuindo em {t}%, o {p} fica: R${moeda.diminuir(p, t)}')


# se der mensagem de erro lá em cima é só colocar -> import ex107.moeda ou from ex107 import moeda
