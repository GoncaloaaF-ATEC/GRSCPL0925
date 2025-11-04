#
# crie um loop for que mostre todos os valores de 0 a 10
#


for i in range(11):
    print(i, end=" ")



"""

range(n) -> mostrar todos os números inteiros de 0 a n-1 --  range(n) <-> range(0, n) <-> range(0, n, 1)
range(m, n) -> mostrar todos os números inteiros de m a n-1 -- range(m, n) <-> range(m, n, 1)
range(m, n, s) -> mostrar todos os números inteiros de m a n-1 com step de s

System.Out.println() <-> print()

"""


#
# crie um app que calcula a tabuada.
# deve pedir ao utilziador que tabuada quer calcular
#
print()
num = int(input("Número para a tabuada: "))

for c in range(1, 11):
    res = num * c
    print(f"{num} x {c} = {res}")


condicao = True













# maquina 2
#btn condicao = False



# condicao =  data_atual > 25-12-2025
# maquina 1
#while condicao:
#    print("ola mundo")



"""


tipos de dados
var
in/out
condiçoes  
    if-elif-else
    match-case

range
loop   
    for   
    while

"""



# +
# -
# /
# *

# % <- modulo (Mod) (resto)

"""

Mod 2 -> 0 1

0 1 2 3 4 5 
0 1 0 1 0 1

"""

# ** -> power
print(2 ** 10) # 2^10
print(pow(2, 10))


# // -> div int

print(10/2) # -> 5.0 (float)

print(10//2) # -> 5 (int) <- descarta a parte decimal


print(11/2) # -> 5.5 (float)


print(11//2) # -> 5 (int) <- descarta a parte decimal