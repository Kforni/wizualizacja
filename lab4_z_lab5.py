import sys

def zad1_lista4():
    lista=[]
    for i in range(1,11):
        lista+=[i*4]
    plik=open("podzielne.txt","a+")
    plik.writelines(str(lista))
    plik.close()

def zad2_lista4(): 
    plik=open("podzielne.txt")
    print(plik.readline())
    plik.close()

def zad3_lista4():
    with open("podzielne.txt", "a+") as plik:
        plik.writelines(['To sa', 'liczby podzielne', 'przez 4'])
    with open("podzielne.txt", "r") as plik:
        print(plik.readline())

#zad6_lista5
class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

def zad6_lista5():
    imie=Wspak('Kamil')
    print(next(imie))
    print(next(imie))
    print(next(imie))

    lista=Wspak([1,2,4,8,16,32,64,128])
    print(next(lista))
    print(next(lista))
    print(next(lista))

    krotka=Wspak((1,4,'cat','dog'))
    print(next(krotka))
    print(next(krotka))
    print(next(krotka))

#zad7_lista5
class Parzysty:
    """Iterator zwracający parzyste wyrazy"""
    def __init__(self, data):
        self.data = data
        self.index = -1
        self.stop = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.stop:
            raise StopIteration
        self.index = self.index + 2
        return self.data[self.index]

def zad7_lista5():
    napis=Parzysty('Python jest spoko')
    print(next(napis))
    print(next(napis))
    print(next(napis))
    liczby=Parzysty([1,2,3,4,5,6])
    print(next(liczby))
    print(next(liczby))
    print(next(liczby))

#zad8_lista5
class Samogloski:
    """Iterator zwracający samogloski z wyrazenia"""
    def __init__(self, data):
        if isinstance(data,str):
            self.data = data
            self.index = 0
            self.stop = len(data)-1
        else:
            return None

    def __iter__(self):
        return self

    samogloski=['A','a','Ą','ą','E','e','Ę','ę','I','i','O','o','Ó','ó','U','u','Y','y']

    def __next__(self):
        if self.index >= self.stop:
            raise StopIteration
        while self.data[self.index] not in self.samogloski:
            #print(self.data[self.index])
            self.index = self.index + 1
        wynik = self.data[self.index]
        self.index = self.index + 1
        return wynik

def zad8_lista5():
    zdanie=Samogloski('Ja mam pro')
    print(next(zdanie))
    print(next(zdanie))
    print(next(zdanie))
    try:
        print(next(zdanie))
    except StopIteration:
        print('String się skończył')

#zad9_lista5
def parzysty_gen(data):
    for index in range(0, len(data), 2):
        yield data[index]

def zad9_lista5():
    gen=parzysty_gen("Parupepy")
    print(next(gen))
    print(next(gen))
    print(next(gen))

#zad10_lista5
import itertools

def itera(data):
    for element in itertools.combinations(data,3):
        yield element

def zad10_lista5():
    a=itera('AbCdEfGhIj')
    print(next(a))
    print(next(a))
    print(next(a))

#zad11_lista5
def fibonacci(n):
    a,b=(0,1)
    for _ in range(n):
        yield a
        a,b=(b,a+b)

def zad11_lista5():
    fibo=fibonacci(10)
    print(list(fibo))

#zad12_lista5
def zad12_lista5():
    import datetime
    import locale
    locale.setlocale(locale.LC_ALL, '')
    polish_months=[datetime.date(1900, x, 1).strftime('%B') for x in range(1,13,1)]
    print(polish_months)

zad1_lista4()
zad2_lista4()
zad3_lista4()
zad6_lista5()
zad7_lista5()
zad8_lista5()
zad9_lista5()
zad10_lista5()
zad11_lista5()
zad12_lista5()