# zad 5 ##################################



# zad 4 ##################################
from math import floor

liczba = input('podaj przez ile liter wyswietlac')

n = floor(26 / int(liczba))
print(n)
for i in range(n):
    print(chr(i*int(liczba)+65),chr(i*int(liczba)+97))

# zad 3 ##################################

for i in range(26):
    print(chr(i+65),chr(i+97))

# zad 2 ##################################

def maximum(a1,b1,c1):
  if(a1 > b1):
    if(a1 > c1):
      print(a1)
    else:
      print(c1)
  else:
    if(b1 > c1):
      print(b1)
    else:
      print(c1)

print('podaj trzy liczby')

a2 = input() 
b2 = input()
c2 = input()

maximum(int(a2),int(b2),int(c2))

# zad 1 ##################################

a = input('podaj imie i nazwisko')
b = input('podaj swoj wiek')

def pelno(k):
  if(k > 17):
    return 'pelnoletni'
  else:
    return 'niepelnoletni'

print('Czesc ',a,' jestes ', pelno(int (b)))
