def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
     def __init__(self,top,bottom):
         self.num = top
         self.den = bottom

     def __str__(self):
         return str(self.num)+"/"+str(self.den)

     def show(self):
         print(self.num,"/",self.den)

     def __add__(self,otherfraction):
         newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)

     def __eq__(self, other):
         firstnum = self.num * other.den
         secondnum = other.num * self.den

         return firstnum == secondnum

     def __multi__(self,other):
         top = self.num *other.num
         bottom = self.den * other.den
         common = gcd(top,bottom)
         return Fraction(top//common,bottom//common)

     def __divide__(self,other):
         top = self.num *other.den
         bottom = self.den * other.num
         common = gcd(top,bottom)
         return Fraction(top//common,bottom//common)
         
     def __subtract__(self,otherfraction):
         newnum = self.num*otherfraction.den - \
                      self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)
         return Fraction(newnum//common,newden//common)



x = Fraction(1,2)
y = Fraction(2,3)
print x.__subtract__(y)
