from math import sqrt

## zad 3 #################################

class Silnik:
  
  def __init__(self):
    self.__pojemnosc = 3.2
    self.__uruchomiony = False
    
  def wlaczS(self):
    self.__uruchomiony = True
    
  def wylaczS(self):
    self.__uruchomiony = False
  
class Reflektor:
  def __init__(self):
    self.__sprawny = True
    self.__swieci = False
    
  def wlaczR(self):
    self.__swieci = True
      
  def wylaczR(self):
    self.__swieci = False
      
  def czy_sprawny(self):
    return self.__sprawny
  
class Hamulec:
  def __init__(self):
    self.__sprawny = True
    self.__wcisniety = False
    
  def hamuj(self):
    self.__wcisniety = True
    
  def nie_hamuj(self):
    self.__wcisniety = False
    
  def czy_sprawny(self):
    return self.__sprawny

class Samochod(Hamulec,Reflektor,Silnik):
  def __init__(self):
    __kolor = "zuwty"
    __numer_rejestracyjny = "student_UMCS"
    
    Hamulec.__init__(self)
    Silnik.__init__(self)
    Reflektor.__init__(self)
  
  def jedz(self):
    self.wlaczS()
    self.wlaczR()
    
  def hamujSamochod(self):
    self.hamuj()

  
    

## zad 2 #################################

class Punkt2D:
  x = None
  y = None
  
  def __init__(self,x,y):
    self.x = x
    self.y = y
    
  def oblicz(self,other):
    return sqrt( pow(self.x - other.x,2) + pow(self.y - other.y,2))
    
class Punkt3D(Punkt2D):
  z = None
    
  def __init__(self,x,y,z):
    super(Punkt3D,self).__init__( x, y)
    self.z = z
    
  def oblicz(self,p3D):
    return sqrt( pow(self.z - p3D.z,2) + pow(super(Punkt3D,self).oblicz(p3D),2))

p2 = Punkt3D(1,2,1)
p3 = Punkt3D(1,6,1)

print(p2.oblicz(p3))


## zad 1 #########################################

class LiczbaZespolona:
  rzecz = None
  uroj = None
  
  def __init__(self,rzecz,uroj):
    self.rzecz = rzecz
    self.uroj = uroj
    
  def __add__(self,other):
    return LiczbaZespolona(self.rzecz + other.rzecz, self.uroj + other.uroj)
    
  def __sub__(self,other):
    return LiczbaZespolona(self.rzecz - other.rzecz, self.uroj - other.uroj)
    
  def __mul__(self,other):
    a1 = self.rzecz * other.rzecz - (self.uroj * other.uroj)
    
    b1 = self.rzecz * other.uroj + self.uroj * other.rzecz
    
    return LiczbaZespolona(a1,b1)
    
  def __truediv__(self,other):
    a2 = (self.rzecz * other.rzecz + self.uroj * other.uroj) / (other.rzecz**2 + other.uroj**2)
    
    b2 = (self.uroj * other.rzecz - self.rzecz * other.uroj) / (other.rzecz**2 + other.uroj**2)
    
    return LiczbaZespolona(a2,b2)
    
  def __str__(self):
    return str(self.rzecz)+" + "+str(self.uroj)+"i"
    
  def __setattr__(self,name,value):
    return object.__setattr__(self, name, value)
    
  def modul(self):
    return sqrt(self.rzecz**2 + self.uroj**2)
    
  def __lt__(self,other):
    return self.modul() < other.modul()

  def __le__(self,other):
    return self.modul() <= other.modul()

  def __eq__(self,other):
    return self.modul() == other.modul()
    
  def __ne__(self,other):
    return self.modul() != other.modul()
    
  def __gt__(self,other):
    return self.modul() > other.modul()
    
  def __ge__(self,other):
    return self.modul() >= other.modul()

liczbaZ = LiczbaZespolona(5,1)
liczbaZ2 = LiczbaZespolona(5,1)

print(liczbaZ2 >= liczbaZ )    

########################################

class A(object):
  def __init__(self,zmienna):
    self.zmienna = zmienna
    print(self.zmienna)
    
  def __add__(self,other):
    return self.zmienna + other.zmienna
    
a = A(5)
b = A(8)
print(a+b)


########################################

class A(object):
  def fun(self):
    print("wyw A")
    
class B(A):
  def fun(self):
    print("wyw B")
    super(B,self).fun()
    
B().fun()

########################################

class Samochod:
  __kolor = None
  
  def setKolor(self,kolor):
    self.__kolor = kolor
    
class Osobowy(Samochod):
  marka = "Mercedes"
  
samochod = Osobowy()
samochod.setKolor('Niebieski')

print("To jest %s %s" % (samochod._Samochod__kolor,samochod.marka))
  
#######################################

class Klasa:
  atr1 = None
  __atr2 = None
  
  def setArt2(self,zmienna):
    self.__atr2 = zmienna
  def setAtr3(self,zmienna):
    self.atr3 = zmienna
  def add(self):
    return self.atr1 + self.__atr2 + self.atr3
    
obiekt = Klasa()
obiekt.atr1 = 5
obiekt.setArt2(8)
obiekt.setAtr3(11)
print(obiekt.add())

