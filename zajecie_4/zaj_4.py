import sys
## zad 4 ##########################

if(sys.argv[3] == '-'):
	tab = []
	tab.append(sys.stdin.readline())
	
	while( tab[-1] != "\n" ):
		tab.append(sys.stdin.readline())
	for x in tab:
		if( sys.argv[4] in x ):
			print(x)
else:
	f = open(sys.argv[3])
	for x in f:
		if( sys.argv[4] in x ):
			print(x)
	f.close()

## zad 3 ##########################
f = open(sys.argv[2])

tekst = f.read()

f.close()
dict = {}
for i in tekst.split():
	if (dict.get(i) == None):
		dict[i] = 1
	else:
		dict[i]+=1

print(dict)

## zad 2 ##########################


f = open(sys.argv[1])

napis1 = f.read()

f.close()


## zad 1 ##########################
def func(napis):
  slownik = {}
  for x in napis.split("\n"):
    k = x.split(": ")
    slownik[k[0]] = k[1]
    print(k[0],k[1])
  return slownik
    
print(func(napis1))

napis1 = """k1: w1
k2: w2
k3: w3"""

print(func(napis1))
