"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa que cria sequência de números (usando variável global)
Data: 29/11/21
Atualização: 06/12/21
"""
#Listas
numeros = []#Lista que recebe os números 

#Entrada e processamento de dados
print("======================================")
print("PROGRAMA QUE GERA SEQUÊNCIA DE NÚMEROS")
print("======================================")
print(" ")
numero_inicial = int(input("Digite o número inicial: "))#Pede para o usuário digitar o número inicial
numero_final = int(input("Digite o número final: "))#Pede para o usuário digitar o número final
subtracao = (numero_final - numero_inicial)#Subtrai o número final pelo inicial
n2 = (numero_inicial)#N2 recebe o numero inicial
n3 = 1#N3 recebe 1
def sequencia ():#Função que gera a sequência
    global subtracao#Traz variável global
    global numeros#Traz variável global
    global n2#Traz variável global
    global n3#Traz variável global
    for n in range (subtracao+1):#Gera a sequencia
        numeros.append(n2)
        n2 += 1
    for nn in range (subtracao+1):#Mostra a sequência
        print(numeros[:n3])
        n3 += 1

#Saída de dados
print(" ")
print("==========")
print("RESULTADOS")
print("==========")
print(" ")        
sequencia()#Chama a função, mostrando a sequência
    
