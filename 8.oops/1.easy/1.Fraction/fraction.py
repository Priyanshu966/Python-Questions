class Fraction:
    def __init__(self,num,deno):
        self.num = num
        self.deno = deno
        self.simplify()

    def print(self):
        if self.deno == 0:
            print("Infinity")
        elif self.num == 0:
            print(0)
        elif self.deno == 1:
            print(self.num)
        else:
            print(f'{self.num}/{self.deno}')

    def simplify(self):
        current = min(self.num,self.deno)
        lcm = 1

        while current > 1:
            if self.num % current == 0 and self.deno % current == 0:
                lcm = current
                break
            current -= 1

        self.num = self.num // lcm
        self.deno = self.deno // lcm

    def add(self,f2):
        new_num = self.num * f2.deno + f2.num * self.deno
        new_deno = self.deno * f2.deno

        self.num = new_num
        self.deno = new_deno
        self.simplify()

    def multiply(self,f2):
        new_num = self.num * f2.num
        new_deno = self.deno * f2.deno
        self.num = new_num
        self.deno = new_deno
        self.simplify()



f1 = Fraction(1,2)
f2 = Fraction(3,4)
f3 = Fraction(2,4)
f1.print()
f2.print()
f1.add(f2)
f1.print()
f2.multiply(f3)
f2.print()


