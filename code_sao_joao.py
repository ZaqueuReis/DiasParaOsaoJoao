def anoBissexto(ano):
  if ano % 400 == 0:
    return True, 366
  elif ano % 100 == 0:
    return False, 365
  elif ano % 4 == 0:
    return True, 366
  return False, 365
def diasAteInicioDoMes(mes, ano):
  if mes == 1:
    return 0
  elif mes == 2:
    return 31
  elif mes == 3:
    return 31 + (29 if anoBissexto(ano)[0] else 28)
  elif mes == 4:
    return 31 + (29 if anoBissexto(ano)[0] else 28) + 31
  elif mes == 5:
    return 31 + (29 if anoBissexto(ano)[0] else 28)  + 31 + 30
  elif mes == 6:
    return 31 + (29 if anoBissexto(ano)[0] else 28) + 31 + 30 + 31
  elif mes == 7:
    return 31 + (29 if anoBissexto(ano)[0] else 28) + 31 + 30 + 31 + 30
  elif mes == 8:
    return 31 + (29 if anoBissexto(ano)[0] else 28) + 31 + 30 + 31 + 30 + 31
  elif mes == 9:
    return 31 + (29 if anoBissexto(ano)[0] else 28)+ 31 + 30 + 31 + 30 + 31 + 31
  elif mes == 10:
    return 31 + (29 if anoBissexto(ano)[0] else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30
  elif mes == 11:
    return 31 + (29 if anoBissexto(ano)[0] else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
  else:
    return 31 + (29 if anoBissexto(ano)[0] else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30

def calculoDias(dia, mes, ano):
  diasNoAno = 0
  diasHoje = diasAteInicioDoMes(mes, ano) + dia
  diasParaSaoJoao = diasAteInicioDoMes(6, ano) + 24
  if diasHoje < diasParaSaoJoao:
    diasQueFaltam = diasParaSaoJoao - diasHoje
  else:
    bolle, diasNoAno = anoBissexto(ano)
    diasQueFaltam = diasNoAno - diasHoje + diasAteInicioDoMes(6, ano + 1) + 24

  if diasQueFaltam == 0:
    print("Viva Sao Joao")
  else:
    print(f"Faltam {diasQueFaltam} dias para o Sao Joao chegar")

dia = int(input())
mes = int(input())
ano = int(input())

diasAteInicioDoMes(mes, ano)
calculoDias(dia, mes, ano)