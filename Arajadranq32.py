class MyList:
    def __init__(self, item):
        self.item = item
        self.l = []


    def __getitem__(self, item):
        return self.l[item]

    def __setitem__(self, item, value):
        self.l[item] = value

    def __delitem__(self, item):
        del self.l[item]

    def __add__(self, item):
        self.l.append(item)

    def append(self, x):
        self.l.append(x)

    def remove(self, x):
        if x in self.l:
             self.l.remove(x)
        else:
            raise ValueError('---')


    def pop(self, x):
        c = self.l[x]
        del self.l[x]
        return c



    def __repr__(self):
        return f'{__class__}: MyList'

    def len(self):
        return len(self.l)


    def sort(self):
        sorted(self.l)


    def __str__(self):
        return f'MyList {self.l}'

    def clear(self):
        self.l.clear()


    def insert(self, x):
        if not isinstance(x, int):
            raise ValueError
        else:
            self.l.insert(x)


    def count(self, x):
        self.l.count(x)
