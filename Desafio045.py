import emoji, time, random

print(f"\033[;1m{'Desafio 045 - Jogo Jokenpô':*^50}\033[;m")
itens = (':fist:', ':hand:', ':v:')

print(emoji.emojize(f'''Selecione o simbolo para jogar
1 - {itens[0]}
2 - {itens[1]}
3 - {itens[2]}''', use_aliases=True))

escolha_user = int(input("Escolha: "))

if escolha_user == 1:
    print(emoji.emojize("\033[;34mVocê escolheu :fist:", use_aliases=True))
if escolha_user == 2:
    print(emoji.emojize("\033[;34mVocê escolheu :hand:", use_aliases=True))
if escolha_user == 3:
    print(emoji.emojize("\033[;34mVocê escolheu :v:", use_aliases=True))

time.sleep(1)
print("\033[;32mComputador jogando ... \033[;m")
time.sleep(1)
escolha_comp = random.randrange(0, 3)
print(emoji.emojize(f"O computador escolheu {itens[escolha_comp]}", use_aliases=True))


if escolha_user == 1 and escolha_comp == 0:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":fist: e :fist:\033[1;33m - Jogo Empatou!!", use_aliases=True))
if escolha_user == 1 and escolha_comp == 1:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":fist: é emprulhado pela :hand:\033[1;31m - Computador Ganhou!!", use_aliases=True))
if escolha_user == 1 and escolha_comp == 2:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":fist: esmaga :v:\033[1;34m - Jogador Ganhou!!", use_aliases=True))


if escolha_user == 2 and escolha_comp == 0:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":hand: embrulha :fist:\033[1;34m - Jogador Ganhou!!", use_aliases=True))
if escolha_user == 2 and escolha_comp == 1:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":hand: e :hand:\033[1;33m - Jogo Empatou!!", use_aliases=True))
if escolha_user == 2 and escolha_comp == 2:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":hand: é cortado pela :v:\033[1;31m - Computador Ganhou!!", use_aliases=True))


if escolha_user == 3 and escolha_comp == 0:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":v: é esmagado pela :fist:\033[1;31m - Computador Ganhou!!", use_aliases=True))
if escolha_user == 3 and escolha_comp == 1:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":v: corta :hand:\033[1;34m - Jogador Ganhou!!", use_aliases=True))
if escolha_user == 3 and escolha_comp == 2:
    print("Processando resultado")
    time.sleep(2)
    print(emoji.emojize(":v: e :v:\033[1;33m - Jogo Empatou!!", use_aliases=True))
