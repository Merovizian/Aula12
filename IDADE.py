from datetime import datetime
import calendar

nascimento = input("Digite a sua idade (dd/mm/aaaa): ")
dia = int(nascimento[0:2])
mes = int(nascimento[3:5])
ano = int(nascimento[6:10])
idade_ano = idade_mes = idade_dia = 0


## Verifica se a pessoa ja nasceu e se a data é possivel
if dia > 31 or mes > 12 or (ano > datetime.now().year or (ano == datetime.now().year and mes > datetime.now().month) or (ano == datetime.now().year and mes == datetime.now().month and dia > datetime.now().day)):
    print("\033[1;31mInforme uma data correta!")
    
## Verifica se o mês tem a quantidade de dias certo
elif dia > (calendar.monthrange(ano,mes)[1]):
        print(f"O Mês {mes} do ano {ano} não tem {dia} dias e sim {calendar.monthrange(ano,mes)[1]} dias\n\033[1;31mInforme uma data correta!")
  
## Calcula a sua idade em dia, mes e anos.
else:    
    idade_ano = datetime.now().year - ano
    idade_mes = datetime.now().month - mes
    idade_dia = datetime.now().day - dia
    if idade_dia < 0:
        idade_mes = idade_mes - 1
        idade_dia = calendar.monthrange(ano,mes)[1] + idade_dia
    if idade_mes < 0:
        idade_ano = idade_ano - 1
        idade_mes = 12 + idade_mes
    
    
    
    
print(f"Você tem {idade_ano} anos, {idade_mes} meses e {idade_dia} dias de vida")
