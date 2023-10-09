class MyShows:
    def __init__(self, name: str, hartak: str, tar: int,actor_list: list, number_s = 1, rating = None):
        self.is_valid_name(name)
        self.is_valid_hartak(hartak)
        self.is_valid_tar(tar)
        self.is_valid_rating(rating)
        self.is_valid_actor_list(actor_list)
        self.is_valid_serial_s(number_s)

        self.__name = name
        self.__hartak = hartak
        self.__tar = tar
        self.__actor_list = actor_list
        self.__number_s = number_s
        self.__rating = rating



    @staticmethod
    def is_valid_name(name):
        if not (type(name) == str):
            raise ValueError('wrong name')
        return type(name) == str


    @staticmethod
    def is_valid_hartak(hartak):
        if not (type(hartak) == str):
            raise ValueError('wrong hartak')
        return type(hartak) == str


    @staticmethod
    def is_valid_tar(tar):
        if not (type(tar) == int and tar > 0):
            raise ValueError('wrong tar')
        return type(tar) == int and tar > 0



    @staticmethod
    def is_valid_serial_s(number_s):
        if not (type(number_s) == int and  number_s >= 1):
            raise ValueError('wrong number_serial')


    @staticmethod
    def is_valid_rating(rating):
        if not rating is None:
            return type(rating) == int and 1 <= rating <= 10
        elif rating is None:
            return True
        raise ValueError('sxal gnahatakan')


    @staticmethod
    def is_valid_actor_list(actor_list):
        if not (type(actor_list) == list and all([isinstance(i, str) for i in actor_list])):
            raise ValueError('wrong actor list')
        return type(actor_list) == list and all([isinstance(i, str) for i in actor_list])


    @property
    def serialsname(self):
        return f'seriali anun {self.__name}'

    @property
    def serialshartak(self):
        return f'hartak {self.__hartak}'


    @property
    def serialstar(self):
        return f'taretif {self.__tar}'

    @property
    def serialsactors(self):
        return f'derasannery anunner {self.__actor_list}'

    @property
    def serials_number_s(self):
        return f'{self.__number_s}'

    @serials_number_s.setter
    def serials_number_s(self, number):
        self.is_valid_serial_s(number)
        self.__number_s = number
        print(f'seriali hamarne {number}')


    @property
    def serials_rating(self):
        return self.__rating

    @serials_rating.setter
    def serials_rating(self, rating):
        self.is_valid_rating(rating)
        self.__rating = rating
        print(f'nor gnahatakan {rating}')

    @serials_rating.deleter
    def serials_rating(self):
        self.__rating = None


    def add(self, anun):
        if not  (type(anun) == str and anun.isalpha):
            raise ValueError('sxal chi avelacvel')
        self.__actor_list.append(anun)


    def rm(self, anun):
        if anun not in self.__actor_list:
            raise ValueError('aydpisi anun chka heracnelu hamar')
        self.__actor_list.remove(anun)

    def informacia(self):
        return f'anun: {self.__name}\nhartak: {self.__hartak}\ntaretiv: {self.__tar}\nderasanneri anunner: {self.__actor_list}\nseriali hamary: {self.__number_s}\nrating: {self.__rating}'



kino = MyShows('ilk', 'netflix', 2000, ['Tom', 'Jon', 'Selena', 'Simon'], 14, 9)
# print(kino.informacia())
kino.rm('Tom')
# print(kino.serialsactors)
kino.serials_rating = 5
print(kino.serials_rating)
kino.serials_rating()

