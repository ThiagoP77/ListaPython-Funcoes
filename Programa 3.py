"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Faça um programa, com uma função que
necessite de três argumentos, e que forneça a soma desses três argumentos.
Data: 06/12/21
"""
#Lista
numeros = []#Lista que recebe os números digitados

#Entrada de dados
print("=======================")
print("SOMA DE TRÊS ARGUMENTOS")
print("=======================")
print(" ")
print("-Informe os números-")
print(" ")

#Processamento de dados
def somaf ():#Função que recebe, soma e mostra os valores
    global numeros#Chama variável global
    for s in range(3):#Pede três números e os armazena na lista
        if (s==0):#Define a ordem como "primeiro" quando s vale 0
            ordem = "primeiro"
        elif(s==1):#Define a ordem como "segundo" quando s vale 1
            ordem = "segundo"
        elif(s==2):#Define a ordem como "terceiro" quando s vale 2
            ordem = "terceiro"
        numero = float(input("Informe o %s número: " %(ordem)))#Pede para o usuário inserir um número
        numeros.append(numero)#Adiciona o número digitado à lista
    soma = sum(numeros)#Soma os números da lista
    print(" ")
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Números digitados: %s." %(numeros))#Mostra os números digitados
    print("Soma dos números: %.2f." %(soma))#Mostra a soma dos números
        
#Saída de dados
somaf()#Chama a função
