class rational:
    def __init__(self, num, den):
        if den != 0:
            self.mun = num
            self.den = den
            self.simplify(self)
        else:
            raise ValueError("mmmm no no no; nuh-uh ")

    def __str__(self):
        return f"{self.num}/{self.den}"

    def simplify(self):
        return "temp"

def main():
    pass


if __name__ == '__main__':
    main()