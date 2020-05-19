print(f"\033[;1m{'*'*10}Desafio 040 - Media de notas{'*'*10}\033[m")
nota_a = float(input("Digite a primeira nota do aluno: "))
nota_b = float(input("Digite a segunda nota do aluno: "))
media = (nota_a + nota_b)/2
print(f"Sua Média: {media}")
if media >= 7:
    print("\033[1;32mParabens! Você foi Aprovado!!")
elif media < 5:
    print("\033[1;31mVocê foi Reprovado!!")
else:
    print("\033[1;33mVocê ficou de Recuperação!!")