import  time
print(f"\033[;1m{'*'*10}Desafio 044 - Calcular o valor de um produto{'*'*10}\033[;m")
valor = float(input("Informe o valor do produto: "))
print("\033[;32mAguarde...\033[;m")
time.sleep(2)
print("Informe o método de pagamento\n1 - Dinheiro ou cheque\n2 - Cartão")
meio = int(input("Informe o metodo de pagamento: "))
meio_cartao = 0

if meio == 1:
    print(f"\nDinheiro ou Cheque\nO valor total da compra com o desconto de 10%: \033[1;34mR${valor*0.9}")
if meio == 2:
    print("Processando...")
    time.sleep(1)
    print("Cartão de Credito\nEscolha uma das opções de parcelamento.")
    print("1 - À Vista\n2 - Parcelar em 2x\n3 - Parcelar em 3x.")
    meio_cartao = int(input("Escolha uma opção: "))
if meio_cartao == 1:
    print(f"À Vista\nTotal da compra com desconto de 10%: \033[1;34mR${valor*0.95}")
if meio_cartao == 2:
    print(f"Parcelado em 2x\nTotal da compra R${valor} com parcelas de: \033[1;34mR${valor/2}")
if meio_cartao == 3:
    print(f"Parcelado em 3x\nValor da compra R${valor} com parcelas de: \033[1;34mR${(valor*1.2)/3}\033[;m totalizando \033[1;34mR${valor*1.2}.")
