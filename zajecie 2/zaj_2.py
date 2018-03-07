from math import sqrt
from math import pow
import random
kr = ()
lista = []
lsr = []
for i in range(10):
  kr = (random.randint(0, 11),random.randint(0, 11))
  lista.append(kr)
  
for i in range(9):
  kr = (sqrt( pow(lista[i][0] - lista[i+1][0],2) +  pow(lista[i][1] - lista[i+1][1],2)),lista[i])
  lsr.append(kr)

sorted(lsr,lsr[0])

print(lsr)

kr = (random.randint(0, 11),random.randint(0, 11))
print(kr)
print(lista)

## zad 4 ####################################

def log_fun(n):
  return (n % 4 == 0)
  
def main_fun(k,n):
  lista = []
  for i in n:
    if k(i):
      lista.append(i)
      
  return lista
      
lst = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

print(main_fun(log_fun,lst))

## zad 2 #####################################

n = int(input('podaj dlugosc ciagu '))

def fib(n):
  f1,f2 = 0,1
  for i in range(n):
    f1,f2 = f2,f1 + f2
    yield f1

lst = [(i) for i in fib(n)  ]

print(lst)

## zad 1 ###################################

napis = 'Ala ma kota'

ls = [(slowo, len(slowo)) for slowo in napis.split()]

print(ls)

## zad 4 ###################################

def generator(n):
  print('Start')
  while n:
    print('Generator stop %d' % n)
    yield n
    print('Generator start %d' % n)
    n -= 1
    
for x in generator(5):
  print('Wywolanie %d' % x)

## zad 3 ###################################

kwadrat = lambda x: x*x
print(kwadrat(2))

## zad 2 ###################################

def f1(n):
  def f2(x):
    return n-x
  return f2
  
res = f1(5)
print(res(10))

## zad 1 ###################################

liczby = range(0,20)
kwadraty = [x**2 for x in liczby]
print(kwadraty)