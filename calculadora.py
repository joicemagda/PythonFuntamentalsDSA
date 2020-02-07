# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3.
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

#Definição da função Adição
def add(x, y):
	return x + y

#Definição da função Subtração
def subtract(x, y):
	return x - y

#Definição da função Multiplicação
def multiply(x, y):
	return x * y

#Definição da função Divisão
def divide(x, y):
	return x / y

#Definindo Menu com Opções
print("Escolha uma opção\n\n"
      "1 - Adição\n"
      "2 - Subtração\n"
      "3 - Multiplicação\n"
      "4 - Divisão\n")

#Entrada dos Dados
opcao = int(input("Escolha uma opção (1/2/3/4): "))
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if opcao == 1:
      print(num1, "+", num2, "=", add(num1,num2))

elif opcao == 2:
      print(num1, "-", num2, "=", subtract(num1,num2))

elif opcao == 3:
      print(num1, "*", num2, "=", multiply(num1,num2))

elif opcao == 4:
      print(num1, "/", num2, "=", divide(num1,num2))

else:
      print("\nOpção Inválida!")