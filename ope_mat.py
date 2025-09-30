# Solicite como entrada dois números e depois realizar uma operação de soma, subtração, multiplicação e divisão entre eles

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))  

operacao = input("Digite a operação (+, -, *, /): ") 

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":   
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operação inválida"
    
if isinstance(resultado, (int, float)):
    print("Resultado:", int(resultado))
else:
    print("Resultado:", resultado)