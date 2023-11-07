import math

def fractionize(n):
    return rational((round(n*1000)),1000)

class rational:

    def __init__(self, num, den, ):
        if type(den) is not int:
            raise ValueError("that uhhh denominator there isnt and integer 🤦")
        if type(num) is not int:
            raise ValueError("that uhhh numererator there isnt and integer 🤦")
        if den != 0:
            self.num = num
            self.den = den
            self.simplify(num, den)
        else:
            raise ValueError("mmmm no no no; nuh-uh 🚫🙅 ")

    def __str__(self):
        if self.den == 1:
            return f"{self.num}"
        else:
            return f"{self.num}/{self.den}"

    def simplify(self, num, den):
        if self.num == 0:
            self.den = 1
        idk = math.gcd(self.num, self.den)
        self.num //= idk
        self.den //= idk
        if self.den < 0:
            self.num *= -1
            self.den *= -1

    def __add__(self, other):
        return rational(((other.den * self.num) + (self.den * other.num)), (self.den * other.den))

    def __neg__(self):
        return f"{-self.num}/{self.den}"

    def __sub__(self, other):
        return rational(((other.den * self.num) + (self.den * -other.num)), (self.den * other.den))

    def __mul__(self, other):
        return rational((self.num * other.num), (self.den * other.den))

    def __invert__(self):
        return f"{self.den}/{self.num}"

    def __truediv__(self, other):
        return rational((self.num * other.den), (self.den * other.num))

    def __float__(self):
        return self.num / self.den

    def __pow__(self, other):
        self.num = self.num**float(other)
        self.den = self.den**float(other)
        return  f"≈ {round((self.num/self.den),3)}"

    def __abs__(self):
        if self.num < 0:
            self.num *= -1
        if self.den < 0:
            self.den *= -1
        return self

    def __radd__(self, other):
        return other + self

    def __rsub__(self, other):
        return other - self

    def __rmul__(self, other):
        return other * self

    def __rtruediv__(self, other):
        return other / self

    def __rpow__(self, other):
        return

    def __eq__(self, other):
        if self.simplify == other.simplify:
            return True

    def __ne__(self, other):
        if self.simplify == other.simplify:
            return False

    def __lt__(self, other):
        if (self.num / self.den) < (other.num / other.den):
            return True
        else:
            return False

    def __gt__(self, other):
        if (self.num / self.den) > (other.num / other.den):
            return True
        else:
            return False

    def __le__(self, other):
        if (self.num / self.den) <= (other.num / other.den):
            return True
        else:
            return False

    def __ge__(self, other):
        if (self.num/self.den) >= (other.num/other.den):
            return True
        else:
            return False

def main():
    fraction1 = rational(2, 5)**rational(1,4)
    print(fraction1 )


if __name__ == '__main__':
    main()
