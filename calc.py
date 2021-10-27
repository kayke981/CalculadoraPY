import time
from decimal import *
import sys
from termcolor import colored, cprint 
from importlib import reload


if int(sys.version[0]) < 3:
   reload(sys)
   sys.setdefaultencoding("utf-8")
  
link_issue = 'https://github.com/kayke981/CalculadoraPY/issues'

def resultado_certo_ou_errado():
  simounão = input('A resposta está certa? [N/Não/Sim/S]: ').lower()
  
  while len(simounão) < 0 or simounão == "" or simounão != 'n' and simounão != 's' and simounão != 'sim' and simounão != 'não':
    simounão = input('A resposta está certa? [N/Não/Sim/S]: ').lower()
  
  if simounão == 'n' or simounão == 'não':
    print('Você pode falar o erro em: ' + link_issue)

def versao():
  cprint('.************************************************.', 'cyan', attrs=['bold'])
  cprint('|          [+] Criado por kayke981               |', 'cyan', attrs=['bold'])
  cprint('|          [+] Versão 0.0.6                      |', 'cyan', attrs=['bold'])
  cprint('|          [+] https://github.com/kayke981       |', 'cyan', attrs=['bold'])
  cprint('|                                                |', 'cyan', attrs=['bold'])
  cprint("'************************************************'", 'cyan', attrs=['bold'])
  


def inicio():
  cprint('\n[NOVO] Colocado as áreas e desenvolvimento para exercícios que exigem desenvolvimento', 'blue', attrs=['bold'])
  cprint('\n[AVISO] Esse projeto NÃO TEM 100% de certeza, estudem que é melhor, não use esse projeto pensando que vai gabaritar na prova, o projeto foi criado para ser algo muito menos sério do que vestibular, prova, simulado. Se estiver fazendo um agora, boa sorte!', 'yellow', attrs=['bold'], file=sys.stderr)
  cprint('[!] A responsabilidade é toda sua, se ir mal em um simulado, prova, vestibular, a culpa não irá ser do projeto, estudem que é melhor :)\n\n', 'red', attrs=['bold'], file=sys.stderr)
  cprint('[1] 2 números\n[2] 3 números\n[11] Potência\n[12] Raiz Quadrada e Cúbica\n[13] Descobrir o raio\n[14] Circunferência (Círculo)\n[15] Diâmetro\n[16] Conversor de medida\n[17] Área do círculo\n[18] Área do quadrado\n[19] Área do triângulo\n[20] Área do retângulo\n[21] Área do losango\n[22] Área do trapézio\n[23] Área da coroa circular\n[exit] exit\n[wiki] Wiki (ajuda)\n\n\n', 'white', attrs=['bold'], file=sys.stderr)

class colors: 
  HEADER = '\033[95m' 
  OKBLUE = '\033[94m' 
  OKCYAN = '\033[96m' 
  OKGREEN = '\033[92m' 
  WARNING = '\033[93m' 
  FAIL = '\033[91m' 
  ENDC = '\033[0m' 
  BOLD = '\033[1m' 
  UNDERLINE = '\033[4m'
versao()
inicio()

escolha = input('Selecione a opção: ').lower()

while len(escolha) < 0 or escolha == "" or escolha != '1' and escolha != '2' and escolha != 'exit' and escolha != '11' and escolha != '12' and escolha != '13' and escolha != '14' and escolha != '15' and escolha != '16' and escolha != 'wiki' and escolha != '17' and escolha != '18' and escolha != '19' and escolha != '20' and escolha != '21' and escolha != '22' and escolha != '23':
  escolha = input('Selecione a opção: ').lower()
  
if escolha == '1':

 calc = str(input('Escolha o número: ')).lower()

 while len(calc) < 0 or calc == "":
  calc = input('Escolha o número: ')

 sinal = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()

 while len(sinal) < 0 or sinal != '+' and sinal != '-' and sinal != '*' and sinal != '/':
    sinal = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()
    
 calc2 = str(input('Escolha o segundo números: ')).lower()

 while len(calc2) < 0 or calc2 == "":
  calc = input('Escolha o número: ')
  
 print(calc, sinal, calc2 + ' = ?')
 
 try:
   if sinal == '+':
     total = Decimal(calc) + Decimal(calc2)
   elif sinal == '-':
     total = Decimal(calc) - Decimal(calc2)
   elif sinal == '*':
     total = Decimal(calc) * Decimal(calc2)
   elif sinal == '/':
     total = Decimal(calc) / Decimal(calc2)
 
   print(calc, sinal, calc2 + ' = ' + str(total))
   resultado_certo_ou_errado()
 except InvalidOperation as err:
   print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)
   
if escolha == '2':

 calc = str(input('Escolha o número: ')).lower()

 while len(calc) < 0 or calc == "":
  calc = input('Escolha o número: ')

 sinal = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()

 while len(sinal) < 0 or sinal != '+' and sinal != '-' and sinal != '*' and sinal != '/':
    sinal = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()
    
 calc2 = str(input('Escolha o segundo número: ')).lower()

 while len(calc2) < 0 or calc2 == "":
  calc = input('Escolha o número: ')
  
 sinal2 = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()

 while len(sinal2) < 0 or sinal2 != '+' and sinal2 != '-' and sinal2 != '*' and sinal2 != '/':
    sinal2 = str(input('Coloque o sinal ["+", "-", "*", "/"]: ')).lower()
 calc3 = str(input('Escolha o terceiro número: ')).lower()

 while len(calc3) < 0 or calc3 == "":
  calc = input('Escolha o número: ')
  
 print(calc, sinal, calc2, sinal2, calc3 + ' = ?')
 
 try:

   if sinal == '+' or sinal2 == '+':
     total = Decimal(calc) + Decimal(calc2) + Decimal(calc3)
   elif sinal == '-' or sinal2 == '-':
     total = Decimal(calc) - Decimal(calc2) - Decimal(calc3)
   elif sinal == '*' or sinal2 == '*':
     total = Decimal(calc) * Decimal(calc2) * Decimal(calc3)
   elif sinal == '/' or sinal2 == '/':
     total = Decimal(calc) / Decimal(calc2) / Decimal(calc3)
 # Possibilidades com "+"
   if sinal == '+':
     if sinal2 == '-':
       total = Decimal(calc) + Decimal(calc2) - Decimal(calc3)
     elif sinal2 == '*':
       total = Decimal(calc) + Decimal(calc2) * Decimal(calc3)
     elif sinal2 == '/':
       total = Decimal(calc) + Decimal(calc2) / Decimal(calc3)
 # Possibilidades com "-"
   if sinal == '-':
     if sinal2 == '+':
       total = Decimal(calc) - Decimal(calc2) + Decimal(calc3)
     elif sinal2 == '*':
       total = Decimal(calc) - Decimal(calc2) * Decimal(calc3)
     elif sinal2 == '/':
       total = Decimal(calc) - Decimal(calc2) / Decimal(calc3)
   # Possibilidades com "*"
   if sinal == '*':
     if sinal2 == '+':
        total = Decimal(calc) * Decimal(calc2) + Decimal(calc3)
     elif sinal2 == '-':
       total = Decimal(calc) * Decimal(calc2) - Decimal(calc3)
     elif sinal2 == '/':
       total = Decimal(calc) * Decimal(calc2) / Decimal(calc3)
    # Possibilidades com "/"
   if sinal == '/':
     if sinal2 == '+':
       total = Decimal(calc) / Decimal(calc2) + Decimal(calc3)
     elif sinal2 ==  '-':
       total = Decimal(calc) / Decimal(calc2) - Decimal(calc3)
     elif sinal2 == '*':
       total = Decimal(calc) / Decimal(calc2) * Decimal(calc3)
   print(calc, sinal, calc2, sinal2, calc3 + ' = ' + str(total))
   resultado_certo_ou_errado()
 except ValueError as err:
   print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)
if escolha == '11':
   potencianum = input('Escolha um número: ')
  
   while len(str(potencianum)) < 0:
    potencianum = input('Escolha um número: ')
  
   potencia = input('Escolha o número da potência: ')
  
   while len(str(potencia)) < 0:
    potencia = Decimal(input('Escolha o número da potência: '))
  
   print(str(potencianum) + '^(' + str(potencia) + ') = ?')
   resultado_certo_ou_errado()
 
   try:
     total = Decimal(potencianum) ** Decimal(potencia)
     print(str(potencianum) + '^(' + str(potencia) + ') =', str(total))
   except ValueError as err:
     print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)

if escolha == '12':
  qouc = input('Raiz Quadrada ou Cúbica? [Quadrada/Cúbica]: ').lower()
  while len(qouc) < 0 or qouc != 'quadrada' and qouc != 'cúbica':
    qouc = input('Raiz Quadrada ou Cúbica? [Quadrada/Cúbica]: ').lower()
    
  if qouc == 'quadrada':
     número = input('Escolha o número: ')
     while len(str(número)) < 0:
      número = input('Escolha o número: ')
     qouc = '²√'
     print(str(qouc) + str(número) + ' = ?')
     resultado_certo_ou_errado()
    
     
     try:
       
       total = Decimal(número) ** Decimal((1/2))
       print(str(qouc) + str(número) + ' =', str(total))
     except ValueError as err:
       print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)
    
     
  elif qouc == 'cúbica':
     número = input('Escolha o número: ')
     while len(str(número)) < 0:
       número = input('Escolha o número: ')
     qouc = '³√'
     print(str(qouc) + str(número) + ' = ?')
     resultado_certo_ou_errado()
    

      
     try: 

       total = Decimal(número) ** Decimal((1/3))
       print(str(qouc) + str(número) + ' =', str(total))
     except ValueError as err:
       print(colors.FAIL + 'Algo deu muito errado, o erro foi: ', err)

if escolha == '13':
  circunferência = input('Coloque o valor da circunferência: ')
  while len(str(circunferência)) < 0:
    circunferência = input('Coloque o valor da circunferência: ')
  
  pi = input('Coloque o valor de π(pi): ')
  while len(pi) < 0:
    pi = input('Coloque o valor de π(pi): ')
  print('R = 2 *', pi, '/', circunferência)
  
  pitotal = 2 * Decimal(pi)
  print('R = ' + str(pitotal), '/', circunferência)
  total = Decimal(circunferência) / Decimal(pitotal)
  print('R = ' + str(total))
  
  resultado_certo_ou_errado()
if escolha == '14':
  pi = input('Coloque o valor de π(pi): ')
  while len(pi) < 0 or pi == "":
    pi = input('Coloque o valor de π(pi): ')
  raio = input('Coloque o valor do raio: ')
  while len(raio) < 0 or raio == "":
    raio = input('Coloque o valor do raio: ')
  print('C = 2 *', pi + ' *', raio)
  pitotal = 2 * Decimal(pi)
  print('C = ' + str(pitotal), '*', raio)
  total = Decimal(pitotal) * Decimal(raio)
  print('C = ' + str(total))
  resultado_certo_ou_errado()
  
if escolha == '15':
  raio = input('Coloque o valor do raio: ')
  
  while len(raio) < 0:
    raio = input('Coloque o valor do raio: ')
  
  print('D =' + str(raio), '* 2')
  total = Decimal(raio) * 2
  print('D = ' + str(total))
  resultado_certo_ou_errado()

if escolha == '16':
   medida = input('Escolha a medida que você deseja [Comprimento/Capacidade/Massa]: ').lower()
  
   while len(medida) < 0 or medida != 'comprimento' and medida != 'capacidade' and medida != 'massa':
     medida = input('Escolha a medida que você deseja [Comprimento/Capacidade/Massa]: ').lower()
  
   if medida == 'comprimento':
     comprimentos = input('Escolha o comprimento que queira converter [mm/cm/dm/m/dam/hm/km]: ').lower()
     while len(comprimentos) < 0 or comprimentos != 'mm' and comprimentos != 'cm' and comprimentos != 'dm' and comprimentos != 'm' and comprimentos != 'dam' and comprimentos != 'hm' and comprimentos != 'km':
       comprimentos = input('Escolha o comprimento [mm/cm/dm/m/dam/hm/km]: ').lower()
    
     comprimentos2 = input('para [mm/cm/dm/m/dam/hm/km]: ').lower()
     while len(comprimentos2) < 0 or comprimentos2 != 'mm' and comprimentos2 != 'cm' and comprimentos2 != 'dm' and comprimentos2 != 'm' and comprimentos2 != 'dam' and comprimentos2 != 'hm' and comprimentos2 != 'km':
       comprimentos2 = input('para [mm/cm/dm/m/dam/hm/km]: ').lower()
    
     quantidade1 = input('Coloque o número: ')
    
     while len(quantidade1) < 0:
       quantidade1 = input('Coloque o número: ')
    
    
     print(quantidade1 + comprimentos, 'para', comprimentos2, '= ?')
    
     
  
     # Possibilidades com "mm"
     if comprimentos == comprimentos2:
       total = Decimal(quantidade1 + comprimentos)
     if comprimentos == 'mm':
      # Multiplicando
      if comprimentos2 == 'cm':
        total = Decimal(quantidade1) * 10
      if comprimentos2 == 'dm':
        total = Decimal(quantidade1) * 100
      if comprimentos2 == 'm':
        total = Decimal(quantidade1) * 1000
      if comprimentos2 == 'dam':
        total = Decimal(quantidade1) * 10000
      if comprimentos2 == 'hm':
        total = Decimal(quantidade1) * 100000
      if comprimentos2 == 'km':
        total = Decimal(quantidade1) * 1000000
    # Possibilidades com 'cm'
     if comprimentos == 'cm':
      # Dividindo
        if comprimentos2 == 'mm':
         total = Decimal(quantidade1) / 10
      # Multiplicando
        if comprimentos2 == 'dm':
         total = Decimal(quantidade1) * 10
        if comprimentos2 == 'm':
         total = Decimal(quantidade1) * 100
        if comprimentos2 == 'dam':
         total = Decimal(quantidade1) * 1000
        if comprimentos2 == 'hm':
         total = Decimal(quantidade1) * 10000
        if comprimentos2 == 'km':
         total = Decimal(quantidade1) * 100000
      # Possibilidades com 'dm'
     if comprimentos == 'dm':
      # Dividindo
       if comprimentos2 == 'mm':
        total = Decimal(quantidade1) / 100
       if comprimentos2 == 'cm':
        total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'm':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'dam':
        total = Decimal(quantidade1) * 100
       if comprimentos2 == 'hm':
        total = Decimal(quantidade1) * 1000
       if comprimentos2 == 'km':
        total = Decimal(quantidade1) * 10000
      # Possibilidades com 'm'
     if comprimentos == 'm':
      # Dividindo
       if comprimentos2 == 'mm':
        total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'cm':
        total = Decimal(quantidade1) / 100
        if comprimentos2 == 'dm':
          total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'dam':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'hm':
        total = Decimal(quantidade1) * 100
       if comprimentos2 == 'km':
        total = Decimal(quantidade1) * 1000
     # Possibilidades com 'dan'
     if comprimentos == 'dam':
       # Dividindo
       if comprimentos2 == 'mm':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'cm':
        total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'dm':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'm':
          total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'hm':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'km':
        total = Decimal(quantidade1) * 100
     # Possibilidades com 'hm'
     if comprimentos == 'hm':
       # Dividindo
       if comprimentos2 == 'mm':
        total = Decimal(quantidade1) / 100000
       if comprimentos2 == 'cm':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'dm':
          total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'm':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'hm':
        total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'km':
        total = Decimal(quantidade1) * 10
     # Possibilidades com 'km'
     if comprimentos == 'km':
       # Dividindo
       if comprimentos2 == 'mm':
        total = Decimal(quantidade1) / 100000
       if comprimentos2 == 'cm':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'dm':
          total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'm':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'hm':
        total = Decimal(quantidade1) / 10
      
     print(quantidade1 + comprimentos, 'para', comprimentos2, '=', str(total) + str(comprimentos))
     resultado_certo_ou_errado()
     
   if medida == 'capacidade':
     comprimentos = input('Escolha o comprimento que queira converter [ml/cl/dl/l/dal/hl/kl]: ').lower()
     while len(comprimentos) < 0 or comprimentos != 'ml' and comprimentos != 'cl' and comprimentos != 'dl' and comprimentos != 'l' and comprimentos != 'dal' and comprimentos != 'hl' and comprimentos != 'kl':
       comprimentos = input('Escolha o comprimento [ml/cl/dl/l/dal/hl/kl]: ').lower()
    
     comprimentos2 = input('para [ml/cl/dl/l/dal/hl/kl]: ').lower()
     while len(comprimentos2) < 0 or comprimentos2 != 'ml' and comprimentos2 != 'cl' and comprimentos2 != 'dl' and comprimentos2 != 'l' and comprimentos2 != 'dal' and comprimentos2 != 'hl' and comprimentos2 != 'kl':
       comprimentos2 = input('para [ml/cl/dl/l/dal/hl/kl]: ').lower()
    
     quantidade1 = input('Coloque o número: ')
    
     while len(quantidade1) < 0:
       quantidade1 = input('Coloque o número: ')
    
    
     print(quantidade1 + comprimentos, 'para', comprimentos2, '= ?')
    
     
  
     # Possibilidades com "mm"
     if comprimentos == comprimentos2:
       total = Decimal(quantidade1 + comprimentos)
     if comprimentos == 'ml':
      # Multiplicando
      if comprimentos2 == 'cl':
        total = Decimal(quantidade1) * 10
      if comprimentos2 == 'dl':
        total = Decimal(quantidade1) * 100
      if comprimentos2 == 'l':
        total = Decimal(quantidade1) * 1000
      if comprimentos2 == 'dal':
        total = Decimal(quantidade1) * 10000
      if comprimentos2 == 'hl':
        total = Decimal(quantidade1) * 100000
      if comprimentos2 == 'kl':
        total = Decimal(quantidade1) * 1000000
    # Possibilidades com 'cm'
     if comprimentos == 'cl':
      # Dividindo
        if comprimentos2 == 'ml':
         total = Decimal(quantidade1) / 10
      # Multiplicando
        if comprimentos2 == 'dl':
         total = Decimal(quantidade1) * 10
        if comprimentos2 == 'l':
         total = Decimal(quantidade1) * 100
        if comprimentos2 == 'dal':
         total = Decimal(quantidade1) * 1000
        if comprimentos2 == 'hl':
         total = Decimal(quantidade1) * 10000
        if comprimentos2 == 'kl':
         total = Decimal(quantidade1) * 100000
      # Possibilidades com 'dm'
     if comprimentos == 'dl':
      # Dividindo
       if comprimentos2 == 'ml':
        total = Decimal(quantidade1) / 100
       if comprimentos2 == 'cl':
        total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'l':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'dal':
        total = Decimal(quantidade1) * 100
       if comprimentos2 == 'hl':
        total = Decimal(quantidade1) * 1000
       if comprimentos2 == 'kl':
        total = Decimal(quantidade1) * 10000
      # Possibilidades com 'm'
     if comprimentos == 'l':
      # Dividindo
       if comprimentos2 == 'ml':
        total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'cl':
        total = Decimal(quantidade1) / 100
        if comprimentos2 == 'dl':
          total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'dal':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'hl':
        total = Decimal(quantidade1) * 100
       if comprimentos2 == 'kl':
        total = Decimal(quantidade1) * 1000
     # Possibilidades com 'dan'
     if comprimentos == 'dal':
       # Dividindo
       if comprimentos2 == 'ml':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'cl':
        total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'dl':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'l':
          total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'hl':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'kl':
        total = Decimal(quantidade1) * 100
     # Possibilidades com 'hm'
     if comprimentos == 'hl':
       # Dividindo
       if comprimentos2 == 'ml':
        total = Decimal(quantidade1) / 100000
       if comprimentos2 == 'cl':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'dl':
          total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'l':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'hl':
        total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'kl':
        total = Decimal(quantidade1) * 10
     # Possibilidades com 'km'
     if comprimentos == 'kl':
       # Dividindo
       if comprimentos2 == 'ml':
        total = Decimal(quantidade1) / 100000
       if comprimentos2 == 'cl':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'dl':
          total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'l':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'hl':
        total = Decimal(quantidade1) / 10
      
     print(quantidade1 + comprimentos, 'para', comprimentos2, '=', str(total) + str(comprimentos))
     resultado_certo_ou_errado()
  
   if medida == 'massa':
     comprimentos = input('Escolha o comprimento que queira converter [mg/cg/dg/g/dag/hg/kg]: ').lower()
     while len(comprimentos) < 0 or comprimentos != 'mg' and comprimentos != 'cg' and comprimentos != 'dg' and comprimentos != 'g' and comprimentos != 'dag' and comprimentos != 'hg' and comprimentos != 'kg':
       comprimentos = input('Escolha o comprimento [mg/cg/dg/g/dag/hg/kg]: ').lower()
    
     comprimentos2 = input('para [mg/cg/dg/g/dag/hg/kg]: ').lower()
     while len(comprimentos2) < 0 or comprimentos2 != 'mg' and comprimentos2 != 'cg' and comprimentos2 != 'dg' and comprimentos2 != 'g' and comprimentos2 != 'dag' and comprimentos2 != 'hg' and comprimentos2 != 'kg':
       comprimentos2 = input('para [mg/cg/dg/g/dag/hg/kg]: ').lower()
    
     quantidade1 = input('Coloque o número: ')
    
     while len(quantidade1) < 0:
       quantidade1 = input('Coloque o número: ')
    
    
     print(quantidade1 + comprimentos, 'para', comprimentos2, '= ?')
    
     
     
  
     # Possibilidades com "mm"
     if comprimentos == comprimentos2:
       total = Decimal(quantidade1 + comprimentos)
     if comprimentos == 'mg':
      # Multiplicando
      if comprimentos2 == 'cg':
        total = Decimal(quantidade1) * 10
      if comprimentos2 == 'dg':
        total = Decimal(quantidade1) * 100
      if comprimentos2 == 'g':
        total = Decimal(quantidade1) * 1000
      if comprimentos2 == 'dag':
        total = Decimal(quantidade1) * 10000
      if comprimentos2 == 'hg':
        total = Decimal(quantidade1) * 100000
      if comprimentos2 == 'kg':
        total = Decimal(quantidade1) * 1000000
    # Possibilidades com 'cm'
     if comprimentos == 'cg':
      # Dividindo
        if comprimentos2 == 'mg':
         total = Decimal(quantidade1) / 10
      # Multiplicando
        if comprimentos2 == 'dg':
         total = Decimal(quantidade1) * 10
        if comprimentos2 == 'g':
         total = Decimal(quantidade1) * 100
        if comprimentos2 == 'dag':
         total = Decimal(quantidade1) * 1000
        if comprimentos2 == 'hg':
         total = Decimal(quantidade1) * 10000
        if comprimentos2 == 'kg':
         total = Decimal(quantidade1) * 100000
      # Possibilidades com 'dm'
     if comprimentos == 'dg':
      # Dividindo
       if comprimentos2 == 'mg':
        total = Decimal(quantidade1) / 100
       if comprimentos2 == 'cg':
        total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'g':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'dag':
        total = Decimal(quantidade1) * 100
       if comprimentos2 == 'hg':
        total = Decimal(quantidade1) * 1000
       if comprimentos2 == 'kg':
        total = Decimal(quantidade1) * 10000
      # Possibilidades com 'm'
     if comprimentos == 'g':
      # Dividindo
       if comprimentos2 == 'mg':
        total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'cg':
        total = Decimal(quantidade1) / 100
        if comprimentos2 == 'dg':
          total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'dag':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'hg':
        total = Decimal(quantidade1) * 100
       if comprimentos2 == 'kg':
        total = Decimal(quantidade1) * 1000
     # Possibilidades com 'dan'
     if comprimentos == 'dag':
       # Dividindo
       if comprimentos2 == 'mg':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'cg':
        total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'dg':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'g':
          total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'hg':
        total = Decimal(quantidade1) * 10
       if comprimentos2 == 'kg':
        total = Decimal(quantidade1) * 100
     # Possibilidades com 'hm'
     if comprimentos == 'hg':
       # Dividindo
       if comprimentos2 == 'mg':
        total = Decimal(quantidade1) / 100000
       if comprimentos2 == 'cg':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'dg':
          total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'g':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'hg':
        total = Decimal(quantidade1) / 10
      # Multiplicando
       if comprimentos2 == 'kg':
        total = Decimal(quantidade1) * 10
     # Possibilidades com 'km'
     if comprimentos == 'kg':
       # Dividindo
       if comprimentos2 == 'mg':
        total = Decimal(quantidade1) / 100000
       if comprimentos2 == 'cg':
        total = Decimal(quantidade1) / 10000
       if comprimentos2 == 'dg':
          total = Decimal(quantidade1) / 1000
       if comprimentos2 == 'g':
          total = Decimal(quantidade1) / 100
       if comprimentos2 == 'hg':
        total = Decimal(quantidade1) / 10
      
     print(quantidade1 + comprimentos, 'para', comprimentos2, '=', str(total) + str(comprimentos))
     resultado_certo_ou_errado()
if escolha == 'wiki':
  cprint('WIKI: \n\nConversor de medidas\nSobre a questão da vírgula eu não sei fazer isso em python ainda, mas a vírgula pela quantidade de casas depois da vírgula, exemplo: 190.5 -> 19,50\n\nPotência\nIndica a multiplicação da base a por ela mesma tantas vezes quanto indicar o expoente, exemplo: 3^(5) = 3 x 3 = 9 x 3 = 27 x 3 = 81 x 3 = 243\n\n', 'white', attrs=['bold'])
if escolha == '17':
  d = input('Coloque o diâmentro: ')
  
  while len(str(d)) < 0 or d == "":
    d = input('Coloque o diâmentro: ')
  pi = input('Coloque o valor de π(pi): ')
  while len(pi) < 0 or pi == "":
    pi = input('Coloque o valor de π(pi): ')
  print('A = ' + d + '²', '*', pi)
  potenciatotal = Decimal(d) ** 2
  print('A = ' + str(potenciatotal), '*', pi)
  total = Decimal(potenciatotal) * Decimal(pi)
  print('A = ' + str(total))
  
  resultado_certo_ou_errado()
if escolha == '18':
  b = input('Coloque a base do quadrado: ')
  while len(b) < 0 or b == "":
    b = input('Coloque a base do quadrado: ')
  b2 = input('Coloque a base do quadrado [padrão=' + b + ']: ')
  if len(b2) < 0 or b2 == "":
    b2 = b
  print('A =', b, '*', b2)
  total = Decimal(b) * Decimal(b2)
  print('A =', str(total))
  resultado_certo_ou_errado()

if escolha == '19':
  h = input('Coloque a altuta do triângulo: ')
  while len(h) < 0 or h == "":
    h = input('Coloque a altuta do triângulo: ')
  b = input('Coloque a base do triângulo: ')
  while len(b) < 0 or b == "":
    b = input('Coloque a base do triângulo: ')
  print('A =', h, '*', b, '/ 2')
  totalMul = Decimal(h) * Decimal(b)
  print('A =', str(totalMul), '/ 2')
  total = totalMul / 2
  print('A =', str(total))
  resultado_certo_ou_errado()

if escolha == '20':
  h = input('Coloque a altura do retângulo: ')
  while len(h) < 0 or h == "":
    h = input('Coloque a altura do retângulo: ')
  b = input('Coloque a base do retângulo: ')
  while len(b) < 0 or b == "":
    b = input('Coloque a base do retângulo: ')
  print('A =', h, '*', b)
  total = Decimal(h) * Decimal(b)
  print('A =', str(total))
  resultado_certo_ou_errado()

if escolha == '21':
  d1 = input('Coloque a diagonal do losango: ')
  while len(d1) < 0 or d1 == "":
    d1 = input('Coloque a diagonal do losango: ')
  d2 = input('Coloque a diagonal do losango [padrão=' + d1 + ']: ')
  if len(d2) < 0 or d2 == "":
    d2 = d1
  print('A =', d1, '*', d2, '/ 2')
  totalMulti = Decimal(d1) * Decimal(d2)
  print('A =', str(totalMulti), '/ 2')
  total = totalMulti / 2
  print('A =', str(total))
  resultado_certo_ou_errado()

if escolha == '22':
  b1 = input('Coloque a primeira base do trapézio: ')
  while len(b1) < 0 or b1 == "":
    b1 = input('Coloque a primeira base do trapézio: ')
  b2 = input('Coloque a segunda base do trapézio: ')
  while len(b2) < 0 or b2 == "":
    b2 = input('Coloque a segunda base do trapézio: ')
  h = input('Coloque a altura do trapézio: ')
  while len(h) < 0 or h == "":
    h = input('Coloque a altura do trapézio: ')
  print('A = (' +  b1, '+', b2 + ') *', h, '/ 2')
  totalSoma = Decimal(b1) + Decimal(b2)
  print('A =', str(totalSoma), '*', h, '/ 2')
  totalMulti = Decimal(totalSoma) * Decimal(h)
  print('A =', str(totalMulti), '/ 2')
  total = Decimal(totalMulti) / 2
  print('A =', str(total))
  resultado_certo_ou_errado()

if escolha == '23':
  r1 = input('Coloque o primeiro raio: ')
  while len(r1) < 0 or r1 == "":
    r1 = input('Coloque o primeiro raio: ')
  r2 = input('Coloque o segundo raio: ')
  while len(r2) < 0 or r2 == "":
    r2 = input('Coloque o segundo raio: ')
  pi = input('Coloque o valor de π(pi): ')
  while len(pi) < 0 or pi == "":
    pi = input('Coloque o valor de π(pi): ')
  print('A =', pi, '* (' + r1 + '²', '-', r2 + '²)')
  r1total = Decimal(r1) ** 2
  r2total = Decimal(r2) ** 2
  totalMenos = Decimal(r1total) - Decimal(r2total)
  print('A =', pi, '*', str(totalMenos))
  total = Decimal(pi) * Decimal(totalMenos)
  print('A =', str(total))
  resultado_certo_ou_errado()
  
