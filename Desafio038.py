print(f"\033[;1m{'*'*10}Desafio 038 - Maior e menor entre dois números{'*'*10}\033[;m")
numero_a = int(input("Digite o primeiro número: "))
numero_b = int(input("Digite o segundo número: "))

if numero_b > numero_a:
    print("O segundo número é maior!")
elif numero_a > numero_b:
    print("O primeiro número é maior!")
else:
    print("Os números são iguais!")