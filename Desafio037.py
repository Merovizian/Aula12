print(f"\033[0;1m{'*'*10}Desafio 037 - Binário Octal Hexadecimal{'*'*10}\033[m")
numero = int(input("Digite um número inteiro: "))
print(f"Você deseja converter \033[34;1m{numero}\033[m para:\n1 - Binário.\n2 - Octal.\n3 - Hexadecimal.")
opção = int(input("Escolha uma opção: "))

if opção == 1:
    print(f"'{numero}' em binário: {bin(numero)[2:]}")
elif opção == 2:
    print(f"'{numero}' em octal: {oct(numero)[2:]}")
elif opção == 3:
    print(f"\n'{numero}' em hexadecimal: {hex(numero)[2:]}")