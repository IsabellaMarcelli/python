def aumentar(preço, taxa):      # não é o mesmo que preço e taxa lá debaixo, aqui é escopo local
    res = preço + (preço * taxa/100)
    return res

def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res 

def dobro(preço):
    res = preço * 2
    return res

def metade(preço):
    res = preço / 2 
    return res
