import os
import random
import time
from termcolor import cprint, colored
import colorama
colorama.init()

def menu():
  os.system('clear')
  cprint('Odgadnij liczbę 0.9', 'cyan')
  cprint('wybierz zakres (wpisz przypisaną liczbę)', 'red')
  cprint('1. od 1 do 10', 'yellow')
  cprint('2. od 1 do 100', 'yellow')
  cprint('3. od 1 do 1000', 'yellow')
  cprint('4. od 1 do 10 000', 'yellow')
  cprint('5. własny zakres (nie działa)','grey')
  menu=input('       ')
  os.system('clear')
  
  

  if menu=='1':
    zl1()
  if menu=='2':
    zl2()
  if menu=='3':
    zl3()
  if menu=='4':
    zl4()
  if menu=='5':
    zl5()


def zl1():
  cprint('Odgadnij liczbę 0.9', 'cyan')
  cprint ('odgadnij liczbę w zakresie od 1 do 10  (Spróbuj mieć jak najmniej punktów)', 'yellow')

  c=random.randint(1,10) 

  score=0

  while True:
    time.sleep(0.5)
    d=input('zgadnij liczbę:')
    time.sleep(0.3)

    int(score)
    score=score+1

    if int(c) == int(d):
      cprint('Wygrałeś! Zgadłeś liczbę! ta liczbza to ' + str(c) + '. Twój wynik to ' + str(score), 'green')
      break
    elif int(c) > int(d):
      cprint('więcej niż ' + d, 'blue')
    elif int(c) < int(d):
      cprint('mniej niż ' + d, 'red')

def zl2():
  cprint('Odgadnij liczbę 0.9', 'cyan')
  cprint ('odgadnij liczbę w zakresie od 1 do 100  (Spróbuj mieć jak najmniej punktów)', 'yellow')

  c=random.randint(1,100)

  score=0

  while True:
    time.sleep(0.5)
    d=input('zgadnij liczbę:')
    time.sleep(0.3)

    int(score)
    score=score+1

    if int(c) == int(d):
      cprint('Wygrałeś! Zgadłeś liczbę! ta liczbza to ' + str(c) + '. Twój wynik to ' + str(score), 'green')
      break
    elif int(c) > int(d):
      cprint('więcej niż ' + d, 'blue')
    elif int(c) < int(d):
      cprint('mniej niż ' + d, 'red')
  
def zl3():
  cprint('Odgadnij liczbę 0.9', 'cyan')
  cprint ('odgadnij liczbę w zakresie od 1 do 1000  (Spróbuj mieć jak najmniej punktów)', 'yellow')

  c=random.randint(1,1000)

  score=0

  while True:
    time.sleep(0.5)
    d=input('zgadnij liczbę:')
    time.sleep(0.3)

    int(score)
    score=score+1

    if int(c) == int(d):
      cprint('Wygrałeś! Zgadłeś liczbę! ta liczbza to ' + str(c) + '. Twój wynik to ' + str(score), 'green')
      break
    elif int(c) > int(d):
      cprint('więcej niż ' + d, 'blue')
    elif int(c) < int(d):
      cprint('mniej niż ' + d, 'red')

def zl4():
  cprint('Odgadnij liczbę 0.9', 'cyan')
  cprint ('odgadnij liczbę w zakresie od 1 do 10 000  (Spróbuj mieć jak najmniej punktów)', 'yellow')

  c=random.randint(1,10000)

  score=0

  while True:
    time.sleep(0.5)
    d=input('zgadnij liczbę:')
    time.sleep(0.3)

    int(score)
    score=score+1

    if int(c) == int(d):
      cprint('Wygrałeś! Zgadłeś liczbę! ta liczbza to ' + str(c) + '. Twój wynik to ' + str(score), 'green')
      break
    elif int(c) > int(d):
      cprint('więcej niż ' + d, 'blue')
    elif int(c) < int(d):
      cprint('mniej niż ' + d, 'red')

def zl5():
  z=0
  z=input('Wpisz w jakim zakresie ma być liczba:')
  os.system('clear')
  
  cprint('Odgadnij liczbę 0.9', 'cyan')
  cprint ('odgadnij liczbę w zakresie od 1 do ' + z + '  (Spróbuj mieć jak najmniej punktów)', 'yellow')

  g=0
  c=random.randint(1,100)
  int(c)
  int(g)
  int(z)
  g=c%z
  score=0

  while True:
    time.sleep(0.5)
    d=input('zgadnij liczbę:')
    time.sleep(0.3)

    int(score)
    score=score+1

    if int(g) == int(d):
      cprint('Wygrałeś! Zgadłeś liczbę! ta liczbza to ' + g + '. Twój wynik to ' + str(score), 'green')
      break
    elif int(d) > int(g):
      cprint('więcej niż ' + d, 'blue')
    elif int(d) < int(g):
      cprint('mniej niż ' + d, 'red')

menu()