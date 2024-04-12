def aumentar(preço = 0, taxa = 0, formatar=False):      
    res = preço + (preço * taxa/100)
    return res if formatar is False else moeda(res) # retorne res padrão se o formatar for falso (não vou formatar
    # ou seja, vai retornar um resultado numérico, se não vai chamar o método moeda e fazer a formatação)

def diminuir(preço = 0, taxa = 0, formatar=False):
    res = preço - (preço * taxa/100)
    return res if formatar is False else moeda(res)

def dobro(preço = 0, formatar=False):
    res = preço * 2
    return res if not formatar else moeda(res)  # mesma coisa da linha 8

def metade(preço = 0, formatar=False):
    res = preço / 2 
    return res if not formatar else moeda(res)

def moeda(preço = 0, moeda = 'R$'):   
    return f'{moeda}{preço:>.2f}'.replace('.', ',')