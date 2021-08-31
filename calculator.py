
#Função Adicionar
def add():
    num1=int(input("Insere um numero: \n"))
    num2=int(input("Insere um segundo numero: \n"))
    soma=num1+num2
    print(soma)

#Função Subtrair
def sub():
    num1 = int(input("Insere um numero: \n"))
    num2 = int(input("Insere um segundo numero: \n"))
    soma = num1 - num2
    print(soma)

#Função Dividir
def div():
    num1 = int(input("Insere um numero: \n"))
    num2 = int(input("Insere um segundo numero: \n"))
    soma = num1 / num2
    print(soma)

#Função Multiplicar
def mult():
    num1 = int(input("Insere um numero: \n"))
    num2 = int(input("Insere um segundo numero: \n"))
    soma = num1 * num2
    print(soma)




print("Bem-Vindo!\n")
print("1-Adicionar\n")
print("2-Subtrair\n")
print("3-Dividir\n")
print("4-Multiplicar\n")
op=int(input("Escolhe uma operacao: \n"))

if(op==1):
    add()
elif(op==2):
    sub()
elif(op==3):
    div()
elif(op==4):
    mult()



