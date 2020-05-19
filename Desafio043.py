print(f"\033[;1m{'*'*10}Desafio 043 - Calculo IMC{'*'*10}\033[;m")
peso = float(input("Infome o seu peso: "))
altura = float(input("Informe a sua altura: "))

imc = peso/(pow(altura,2))

if imc < 18.5:
    print(f"IMC: {imc}\n\033[1;33mVocê está abaixo do peso!")
elif imc < 25:
    print(f"IMC: {imc}\n\033[1;34mVocê está no peso ideal!")
elif imc < 30:
    print(f"IMC: {imc}\n\033[1;33mVocê está com sobrepeso!")
elif imc < 40:
    print(f"IMC: {imc}\n\033[1;33mObesidade! \033[1;31mCuidado!")
else:
    print(f"IMC: {imc}\n\033[1;31mOBESIDADE MÓRBIDA!\nProcure um Médico Imediatamente!!")