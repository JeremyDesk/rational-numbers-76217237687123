import math


class rational:

    def __init__(self, num, den):
        if type(den) is not int:
            raise ValueError("that uhhh denominator there isnt and integer 🤦")
        if type(num) is not int:
            raise ValueError("that uhhh numererator there isnt and integer 🤦")
        if den != 0:
            self.num = num
            self.den = den
            self.simplify(num, den)
        else:
            raise ValueError("mmmm no no no; nuh-uh ")

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



def main():
    fraction = rational(int(input("numerator:")), int(input("denominator:")))
    print(fraction)


if __name__ == '__main__':
    main()
