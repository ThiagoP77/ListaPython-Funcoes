"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Faça um programa com uma função chamada soma Imposto.
A função possui dois parâmetros formais: taxa Imposto,
que é a quantia de imposto sobre vendas expressa em porcentagem e
custo, que é o custo de um item antes do imposto.
A função “altera” o valor de custo para incluir o imposto sobre vendas.
Data: 06/12/21
"""
#Entrada de dados
print("============================")
print("PROGRAMA QUE CALCULA IMPOSTO")
print("============================")
print(" ")
preco = float(input("Informe o preço do produto: "))#Pede para o usuário inserir o preço do produto
print(" ")

#Processamento de dados
def imposto ():#Função que calcula o imposto e preço final
    global preco#Chama a variável global
    if (preco<=900):#Define imposto de 0% quando o produto custa menos de 900 reais
        taxa_preco = "0%"
        precoa = 0
    elif (preco>900)and(preco<=1500):#Define imposto de 5% quando o produto custa entre 900 e 1500 reais
        taxa_preco = "5%"
        precoa = ((preco/100)*5)
    elif (preco>1500)and(preco<=2500):#Define imposto de 10% quando o produto custa entre 1500 e 2500 reais
        taxa_preco = "10%"
        precoa = ((preco/100)*10)
    elif(preco>2500):#Define imposto de 25% quando o produto custa mais de 2500 reais
        taxa_preco = "20%"
        precoa = ((preco/100)*20)
    novo_preco = (preco+precoa)#Calcula o valor final com imposto
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Preço do produto: R$%.2f." %(preco))#Mostra o preço
    print("Porcentagem de imposto: %s." %(taxa_preco))#Mostra a porcentagem de imposto
    print("Valor do imposto: R$%.2f." %(precoa))#Mostra o valor do imposto
    print("Preço depois do imposto: R$%.2f." %(novo_preco))#Mostra o valor final

#Saída de dados
imposto()#Chama a função
