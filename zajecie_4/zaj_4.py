import sys
import string
## zad 5 ##########################

f = open(sys.argv[1])
f2 = open(sys.argv[2],'w')

alf_small = string.ascii_lowercase
alf_big = string.ascii_uppercase

slide = 0

for x in f:
	for c in x:
		if( c in alf_small ):
			f2.write( alf_small[(alf_small.index(c)+slide) % len(alf_small)] )
		elif( c in alf_big ):
			f2.write( alf_big[(alf_big.index(c)+slide) % len(alf_big)] )
		else:
			f2.write( c )
f2.close()
f.close()

## zad 4 ##########################

if(sys.argv[1] == '-'):
	tab = []
	tab.append(sys.stdin.readline())
	
	while( tab[-1] != "\n" ):
		tab.append(sys.stdin.readline())
	for x in tab:
		if( sys.argv[2] in x ):
			print(x)
else:
	f = open(sys.argv[1])
	for x in f:
		if( sys.argv[2] in x ):
			print(x)
	f.close()
## zad 3 ##########################
f = open(sys.argv[1])

tekst = f.read()

f.close() 
dict = {}
for i in tekst.split():
	if (dict.get(i) == None):
		dict[i] = 1
	else:
		dict[i]+=1

slowo = input('wpisz słowo')
print(dict.get(slowo))

## zad 1, zad 2 ##########################
def func(napis):
  slownik = {}
  for x in napis.split("\n"):
    k = x.split(": ")
    slownik[k[0]] = k[1]
  return slownik
    

f = open(sys.argv[1])

napis1 = f.read()

f.close()

print(func(napis1))

napis1 = """k1: w1
k2: w2
k3: w3"""

print(func(napis1))
