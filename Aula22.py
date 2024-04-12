from uteis import fatorial, dobro   # a versão com o from não é recomendada

num = int(input("Digite um valor: "))
#fat = uteis.fatorial(num)              quando uso "from uteis import ...." em vez de "import uteis" na linha do fatorial e dobro não preciso mais de uteis. 
fat = fatorial(num) 
print(f"O fatorial de {num} é {fat}")
#print(f"O dobro de {num} é {uteis.dobro(num)}")
print(f"O dobro de {num} é {dobro(num)}")

