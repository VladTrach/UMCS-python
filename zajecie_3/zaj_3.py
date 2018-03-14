trach.vladyslav@gmail.com#############################################

from math import sqrt

class Punkt2D:
  x = 0
  y = 0
  
  def __init__(self,x,y):
    self.x = x
    self.y = y
    
  def oblicz(self,other):
    return sqrt( pow(self.x - other.x,2) + pow(self.y - other.y,2))
    
class Punkt3D(Punkt2D):
  z = 0
    
  def __init__(self,x,y,z):
    super(Punkt3D,self).__init__( x, y)
    self.z = z
    
  def oblicz(self,p3D):
    return sqrt( pow(self.z - p3D.z,2) + pow(super(Punkt3D,self).oblicz(p3D),2))

p2 = Punkt3D(1,2,1)
p3 = Punkt3D(1,6,1)

print(p2.oblicz(p3))
print()
########################################

class LiczbaZespolona:
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