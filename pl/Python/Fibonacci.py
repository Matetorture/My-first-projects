import os
from termcolor import cprint, colored
import colorama
colorama.init()

os.system('clear')
ilosc=20
ilosc=int(input(colored('Ile pokazać liczb z Ciąg Fibonacciego: ', 'green')))
ilosc_3=int(ilosc/3)
resz=ilosc%3
a=0
b=1
c=1
z=0


while True:
  if ilosc_3==z:
    break
  
  cprint(a, 'yellow')
  b=a+c
  cprint(b, 'red')
  c=a+b
  cprint(c, 'cyan')
  a=c+b
  z=z+1
  if ilosc_3==z: 
    if resz==1:
      cprint(a, 'yellow')
      b=a+c
      
      break
    elif resz==2:
      cprint(a, 'yellow')
      b=a+c
      cprint(b, 'red')
      c=a+b
      
      break
  

  