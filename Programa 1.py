"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Programa que cria sequência de números (usando variável local)
Data: 29/11/21
Atualização: 06/12/21
"""
#Entrada e processamento de dados
print("======================================")
print("PROGRAMA QUE GERA SEQUÊNCIA DE NÚMEROS")
print("======================================")
print(" ")
def sequencia ():#Função que gera a sequencia
    numero_inicial = int(input("Digite o número inicial: "))#Pede para o usuário digitar o número inicial
    numero_final = int(input("Digite o número final: "))#Pede para o usuário digitar o número final
    subtracao = (numero_final - numero_inicial)#Subtrai o número final pelo inicial
    for n in range (subtracao + 1):#Gera a sequencia
        if (n==0):#Mostra o front-end na primeira vez que o "for" roda
            print(" ")
            print("==========")
            print("RESULTADOS")
            print("==========")
            print(" ")
        print(str(numero_inicial)*numero_inicial)
        numero_inicial += 1#Adiciona 1 ao número inicial

#Saída de dados
sequencia()#Chama a função, mostrando a sequencia
