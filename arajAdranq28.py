class BankUser:
    def __init__(self, name, firstname, age, codenumber, balance, password):
        if not (self.nf(name, firstname) and self.t(age) and self.num(codenumber) and self.bal(balance) and self.p(password)):
            raise ValueError('Սխալ կրկին ստուգեք ձեր մուտքագրած տվյալները')
        self._name = name
        self._firstname = firstname
        self._age = age
        self.__codenumber = codenumber
        self.__balance = balance
        self.__password = password
        self.k = 0





    @staticmethod
    def nf(name, firstname):
        return name.isalpha() and firstname.isalpha()


    @staticmethod
    def t(age):
        return type(age) == int and age > 0
    @staticmethod
    def num(codenumber):
        if type(codenumber) == str and len(codenumber) == 16:
            return len(codenumber) == 16 and codenumber.isdecimal()
        elif type(codenumber) == str and len(codenumber) == 19 and (codenumber[4] + codenumber[9] + codenumber[14]) == '   ' and codenumber.count(' ') == 3:
                c = codenumber.replace(' ', '')
                return c.isdecimal()

    @staticmethod
    def bal(balance: int):
        return balance > 0

    @staticmethod
    def p(password: str):
        return type(password) == str and len(password) >= 8


    def na(self):
        return f'Անուն Ազգանուն: {self._name} {self._firstname}'

    def tariq(self):
        return f'Ձեր տարիքը։ {self._age}'

    def hsh(self):
        while True:
            a = input('Մուտքագրեք ձեր Գաղտնաբսռը')
            if a == self._BankUser__password:
                return f'հաշվեհամարը։ {self._BankUser__codenumber} հաշվեկշիռ։ {self._BankUser__balance}'
            if a != self._BankUser__password:
                 self.k += 1
                 print('Սխալ է')
            if self.k == 3:
                del BankUser
                print('ձեր քարտը ԱՐԳԵԼԱՓԱԿՎԱԾ Է')
                break


    def gum(self, l:int):
        self._BankUser__balance += l
        print(f'Ձեր հաշվեկշիռը ավելացավ {l} դրամով')

    def han(self, m):
        if self._BankUser__balance - m < 0:
            return 'անբավարար հաշվեկշիռ'
        self._BankUser__balance -= m
        print(f'Ձեր հաշվեկշիռը պակասեց {m} դրամով')




Gevorg = BankUser('NAREK', 'MARGARYAN', 20, '1645 5445 6897 1234', 15000, 'NKdfd5555')

print(Gevorg.tariq())
print(Gevorg.hsh())
print(Gevorg.na())
print(Gevorg.tariq())
