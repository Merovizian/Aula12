print(f"\033[;1m{'*'*10}Desafio 036 - Condições para emprestimo{'*'*10}\033[0m")
valor_casa = float(input("Informe o valor da casa: "))
valor_salario = float(input("Informe o seu salário: "))
tempo = int(input("Informe em quantos meses quer pagar a casa: "))

prestação = valor_casa / tempo


if prestação <= (valor_salario*0.3):
    print(f"\033[1;34mEmprestimo Aceito!!\n\033[mA prestação será de \033[1;34mR$ {prestação:.2f}.")
else:
    print(f"\033[;31mEmpréstimo Negado!\n\033[mSua prestação está \033[1;31mR$ {prestação - valor_salario*0.3:.2f} \033[macima dos 30% do seu salário.\nTente novamente escolhendo uma casa mais barata ou aumentando as prestações.")