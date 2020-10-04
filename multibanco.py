import sys


class Conta:	#Criação da class

	def __init__(self,nr,saldo=0):  #Construtor Obrigatório
		self.nr = nr
		self.saldo = saldo

	def deposito(self, valor):
		self.saldo+=valor

	def levantamento(self,valor):
		self.saldo-=valor

	def getSaldo(self):
		return self.saldo

	def getNrConta(self):
		return self.nr



conta1=Conta(1,25)  #Criação do Objeto

print("bem vindo ao MultiBanco")

while True:

	print("1-Consultar\t 2-Depositar\t 3-levantar\t 4-Sair")  #Menu
	opcao=int(input("Escolhe uma opção"))


	if opcao==1:
		print("O saldo da conta é €{:,.2f}".format(conta1.getSaldo()))

	elif opcao==2:
		valor = float(input("Indique o valor a depositar:"))
		confirm=input("Pretende fazer este deposito Sim ou Nao:")
		if confirm == "Sim":
			conta1.deposito(valor)
			print("O saldo da conta é €{:,.2f}".format(conta1.getSaldo()))
		else:
			print("Operação Cancelada")

	elif opcao==3:
		valor = float(input("Indique o valor a levantar"))
		confirm = input("Pretende fazer este levantamento Sim ou Nao:")
		if confirm == "Sim":
				print("Verificação de provisão")
				if valor>=conta1.getSaldo():
					print("O saldo é infrior ao valor a levantar")
				else:
					conta1.levantamento(valor)
					print("O saldo da conta é €{:,.2f}".format(conta1.getSaldo()))
		else:
			print("Operação Cancelada")

	elif opcao==4:
		print("Obrigado pera preferência, volte sempre")
		sys.exit(0)

	else:
		print("Opção Inválida")


