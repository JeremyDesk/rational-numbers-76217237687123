import math
class rational:
    def __init__(self, num, den):
        if den != 0:
            self.num = num
            self.den = den
            self.simplify(num,den)
        else:
            raise ValueError("mmmm no no no; nuh-uh ")

    def __str__(self):
        return f"{self.num}/{self.den}"
    def simplify(self,num,den):
        idk = math.gcd(self.num,self.den)
        self.num = int(self.num/idk)
        self.den = int(self.den/idk)

def main():
    fraction=rational(2,0)
    print(fraction)

if __name__ == '__main__':
    main()