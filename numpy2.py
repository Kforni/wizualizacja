import numpy as np

array1=np.linspace(3,6,3)
array2=np.linspace(0,4,3)

def zad1(array1,array2):
    print (array1*array2)

#zad2
def zad2():
    a=np.arange(0,9).reshape(3,3)
    b=np.arange(10,26).reshape(4,4)
    print(a)
    print(a.min(axis=0))
    print(a.min(axis=1))
    print(b)
    print(b.min(axis=0))
    print(b.min(axis=1))

#zad3
def zad3(array1,array2):
    print (array1.dot(array2))

def zad4():
    v1=np.arange(4,7)
    v2=np.array([np.sqrt(3), np.pi, 4.523])
    print(v1*v2)

def zad5():
    v = np.arange(6).reshape(2,3)
    a = np.sin(v)
    return a

def zad6():
    v = np.arange(6).reshape(2,3)
    b = np.cos(v)
    return b

def zad7(a,b):
    print (a+b)

def zad8():
    a=np.arange(3,12).reshape(3,3)
    for i in a:
        print (i) 

def zad9():
    a=np.arange(666,675).reshape(3,3)
    for i in a.flat:
        print (i) 

def zad10():
    a=np.arange(81).reshape(9,9)
    #mamy 5 możliwości
    #w kazdym przypadku liczbą wierszy i kolumn są dzielniki 81,
    #które po wymnożeniu dadzą 81
    #w innych wypadkach macierz nie zostanie poprawnie wypełniona 
    a.reshape(1,81)
    a.reshape(3,27)
    a.reshape(9,9)
    a.reshape(27,3)
    a.reshape(81,1)

def zad11():
    a=np.arange(12)
    a=a.reshape(3,4)
    for i in a.flat:
        print(i)
    a=a.reshape(4,3)
    for i in a.flat:
        print(i)
    a=a.reshape(2,6)
    for i in a.flat:
        print(i)
    #tak, wyniki są identyczne

zad1(array1,array2)
zad2()
zad3(array1,array1)
zad4()
zad5()
zad6()
zad7(zad5(),zad6())
zad8()
zad9()
zad10()
zad11()
