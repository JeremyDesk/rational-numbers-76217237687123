import math
class rational:
    def __init__(self, num, den):
        if den != 0:
            self.num = num
            self.den = den
            self.simplify(self)
        else:
            raise ValueError("mmmm no no no; nuh-uh ")

    def __str__(self):
        return f"{self.num}/{self.den}"
    def simplify(self):
        idk = math.gcf(self.num,self.den)
        self.num = self.num/idk
        self.den = self.dem/idk

def main():
    fraction=(2,4)
    print(fraction)

if __name__ == '__main__':
    main()