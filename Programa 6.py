"""
Nome do programador: Thiago Piffer Lauro
Nome do programa: Faça um programa que converta da notação de 24 horas para a
notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
A entrada é dada em dois inteiros. Deve haver pelo menos duas funções:
uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M.
como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as
conversões terá um parâmetro formal para registrar se é A.M. ou P.M.
Inclua um loop que permita que o usuário
repita esse cálculo para novos valores de entrada todas as vezes que desejar.
Data: 06/12/21
"""
#Variável
continuar = "Sim"#Variável que garante que o programa continue funcionando

#Funções/Processamento de dados
def horac ():#Função que converte a hora
    global hora#Chama variável global
    global minuto#Chama variável global
    if (hora>12):#Muda a hora e define a terminação como "P.M." quando a hora é maior que 12
        hora2 = (hora-12)
        terminacao = "P.M."
        return ("%d:%d %s" %(hora2, minuto, terminacao))#Retorna esse formato de hora como resultado
    else:#Define a terminação como "A.M." quando a hora é menor que 12
        hora2 = hora
        terminacao = "A.M."
        return ("%d:%d %s" %(hora2, minuto, terminacao))#Retorna esse formato de hora como resultado

def resultado ():
    global hora#Chama variável global
    global minuto#Chama variável global
    print("=========")
    print("RESULTADO")
    print("=========")
    print(" ")
    print("Hora digitada: %d:%d." %(hora, minuto))#Mostra a hora digitada
    print("Hora convertida: %s" %(horac()))#Mostra a hora convertida (retorno da função de conversão)
    
#Entrada e saída de dados
print("==========================")
print("PROGRAMA QUE CONVERTE HORA")
print("==========================")
print(" ")
while(continuar=="Sim")or(continuar=="S")or(continuar=="sim")or(continuar=="s")or(continuar=="SIM"):#Garante que o programa possa se repetir
        hora = int(input("Informe somente as horas: "))#Pede para o usuário inserir a hora
        if(hora<0) or (hora>24):#Pula uma linha quando a nota é invalida
            print(" ")
        while(hora<0) or (hora>24):#Exige hora válida
            print("Hora inválida!")
            hora = int(input("Informe uma hora (entre 0 e 24): "))#Pede para o usuário inserir a hora
            print(" ")
        minuto = int(input("Informe somente os minutos: "))#Pede para o usuário inserir os minutos
        print(" ")
        while(minuto<0) or (minuto>=60):#Exige minutos válidos
            print("Minutos inválidos!")
            minuto = int(input("Informe um minuto (entre 0 e 59): "))#Pede para o usuário inserir os minutos
            print(" ")
        resultado()#Chama a função com os resultados
        print(" ")
        continuar = str(input("Deseja continuar usando o programa? "))#Pergunta se o usuário deseja repetir o programa
        print(" ")
print(" ")
print("Agradeço por utilizar esse programa!")
