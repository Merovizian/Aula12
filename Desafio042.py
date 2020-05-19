print(f"\033[;1m{'*'*10}Desafio 042 - Que tipo de triangulo é{'*'*10}\033[0;m")
reta_a = int(input("Digite o tamanho do lado a: "))
reta_b = int(input("Digite o tamanho do lado b: "))
reta_c = int(input("Digite o tamanho do lado c: "))

if (reta_a + reta_b > reta_c) and (reta_a + reta_c > reta_b) and (reta_b + reta_c > reta_a):
    if reta_a == reta_b == reta_c:
        print("Triângulo Equilátero")
    elif (reta_a == reta_b) or reta_a == reta_c or reta_b == reta_c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("\033[1;31mNão Forma Triângulo")