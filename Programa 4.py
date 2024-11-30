"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Faça um programa, com uma função que necessite de um
argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
Data: 06/12/21
"""
#Entrada de dados
print("=============================================")
print("PROGRAMA QUE VERIFICA SE UM NÚMERO É POSITIVO")
print("=============================================")
print(" ")
numero = float(input("Informe o número: "))#Pede para o usuário inserir um número
print(" ")

#Processamento de dados
def verificar (x):#Função que verifica se o número digitado é nulo, positivo ou negativo
    if (x>0):#Retorna "P" se for positivo
        return "P"
    else:#Retorna "N" se for negativo ou nulo
        return "N"
    
#Saída de dados
print("=========")
print("RESULTADO")
print("=========")
print(" ")
print("O número é: %s." %(verificar(numero)))#Mostra o retorno definido na função
