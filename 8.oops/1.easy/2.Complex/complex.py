class Complex:
    def __init__(self,real,imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return "This is a class for creating Complex Numbers"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        new_real = (self.real * other.real) - (self.imaginary * other.imaginary)
        new_imaginary = (self.real * other.imaginary) + (self.imaginary * other.real)
        return Complex(new_real, new_imaginary)

    def add(self,other):
        new_real = self.real + other.real
        new_imaginary = self.imaginary + other.imaginary
        self.real = new_real
        self.imaginary = new_imaginary

    def print(self):
        real = self.real
        imaginary = self.imaginary
        if real == 0 and imaginary == 0:
            print(0)
        elif real == 0:
            print(f'{imaginary}i')
        elif imaginary == 0:
            print(f'{real}')
        elif imaginary > 0:
            if imaginary == 1:
                print(f'{real} + i')
            else:
                print(f'{real} + {imaginary}i')
        elif imaginary < 0:
            if imaginary == -1:
                print(f'{real} - i')
            else:
                print(f'{real} - {-1 * imaginary}i')


c1 = Complex(2,3)
c2 = Complex(4,5)
c3 = c1 + c2
c3.print()
c4 = c1 * c2
c4.print()