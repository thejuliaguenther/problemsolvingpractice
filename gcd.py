class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def gcd(self):
        x = self.num
        y = self.den
        while x % y != 0:
            oldx = x
            oldy = y

            x = oldy
            y  = oldx % oldy

        print y      