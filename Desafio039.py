from datetime import datetime
import calendar

print(f"\033[;1m{'*'*10}Desafio 039 - Idade para alistamento {'*'*10}\033[m")
nascimento = input("Informe sua data de nascimento(dd/mm/aaaa): ")
dia = int(nascimento[0:2])
mes = int(nascimento[3:5])
ano = int(nascimento[6:10])

if (datetime.now().year - ano) > 18:
    print(f"\033[1;31mJá passou da hora de alistar!\033[;m\nProcure uma unidade Imediatamente!\nPassaram-se {(datetime.now().year - ano) - 18} anos")
elif (datetime.now().year - ano) < 18:
    print("\033[;32mFicamos contente com sua disposição, Mas você não precisa se alistar este ano!")
elif (mes - datetime.now().month) > 1 and dia > datetime.now().day:
    print(f"\033[1;33mSeu alistamento será este ano!\033[;m\nFaltam {(mes - datetime.now().month)-1} meses", f"e {dia - datetime.now().day} dias!" if (dia - datetime.now().day!=0) else "")
elif (mes - datetime.now().month) == 1 and dia >= datetime.now().day:
    print(f"\033[1;33mSeu alistamento será este ano!\033[;m\nFalta 1 mes!", f"e {dia-datetime.now().day} dias" if (dia -datetime.now().day != 0) else"")
elif (mes - datetime.now().month) == 1 and dia <= datetime.now().day:
    print(f"\033[1;33mSeu alistamento será no próximo mês!\033[1;31m\nFaltam {(calendar.monthrange(ano, (datetime.now().month)))[1] - datetime.now().day + dia } dias")
elif (datetime.now().day == dia):
    print(f"\033[1;31mSeu alistamento vence Hoje!\033[1;33m\nCorra para uma agência!")
elif (dia - datetime.now().day) == 1 and datetime.now().month == mes:
    print(f"\033[1;33mSeu alistamento será Amanhã\033[;m\nPor Favor Procure uma agência")
elif (dia - datetime.now().day) > 1 and datetime.now().month == mes:
    print(f"\033[1;33mSeu alistamento será este mês!\033[;m\n\033[1;31mFaltam {dia - datetime.now().day} dias")
elif datetime.now().month == mes:
    print(f"\033[1;31mJá passou da hora de alistar!\033[;m\nProcure uma unidade Imediatamente!\nPassaram {datetime.now().day - dia} dias")
elif datetime.now().year - ano == 18:
    print( f"\033[1;31mJá passou da hora de alistar!\033[;m\nProcure uma unidade Imediatamente!\nPassaram {datetime.now().month - mes} mêses")



