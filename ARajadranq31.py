class Calculator:
    def __init__(self, args):
        if not isinstance(args, int|float|Calculator):
            raise TypeError('Invalid number')
        self.__args = args


    @property
    def number(self):
        return self.__args

    def __add__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __ADD__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args + other

    def __radd__(self, other):
        return self + other


    def __iadd__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('---iadd')
        if isinstance(other, Calculator):
            other = other.__args
        self.__args += other


    def __sub__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('__SUB___')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args - other

    def __rsub__(self, other):
        return self - other

    def __isub__(self,other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __ISUB__')
        if isinstance(other, Calculator):
            other = other.__args
        self.__args -= other

    def __mul__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __MUL__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args * other


    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __IMUL__')
        if isinstance(other, Calculator):
            other = other.__args
        self.__args *= other


    def __truediv__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __TRUEDIV__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args / other

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __ITRUEDIV__')
        if isinstance(other, Calculator):
            other = other.__args
        self.__args /= other

    def __floordiv__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __FLOORDIV__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args // other

    def __rfloordiv__(self, other):
        return self // other



    def __ifloordiv__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __IFLOORDIV__')
        if isinstance(other, Calculator):
            other = other.__args
        self.__args //= other

    def __mod__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __MOD__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args % other

    def __rmod__(self, other):
        return self % other

    def __imod__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __IMOD__')
        if isinstance(other, Calculator):
            other = other.__args
        self.__args %= other

    def __pow__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __POW__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args ** other

    def __rpow__(self, other):
        return self + other

    def __ipow__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __IPOW__')
        if isinstance(other, Calculator):
            other = other.__args
        self.__args **= other

    def __eq__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __EQ__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args == other

    def __lt__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __LT__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args < other

    def __le__(self, other):
        if not isinstance(other, int|float|Calculator):
            raise TypeError('ERROR __LE__')
        if isinstance(other, Calculator):
            other = other.__args
        return self.__args <= other


    def __str__(self):
        return f'{self.__args}'

    def __repr__(self):
        return f'{(self.__class__)} : {self.__args}'


c1 = Calculator(100)
c2 = Calculator(5)
# print(c1.number)
# print(c1 / c2)
print(c1)
print(c1 / c2)
print(repr(c1))