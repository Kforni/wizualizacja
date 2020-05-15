import sys
import math

def zad1():
    print(input('Podaj mi zdanie, zwróce Ci spacje\n').count(' '))
def zad2():
    print ('Podaj pierwszą liczbę')
    pierwsza=sys.stdin.readline()
    pierwsza=int(pierwsza)
    print ('Podaj drugą liczbę')
    druga=sys.stdin.readline()
    druga=int(druga)
    sys.stdout.write(str(pierwsza*druga))
#Zad3
def zad4():
    print('Wartość bezwzgledna z podanej liczby to ' +str(abs(float(input('Podaj liczbe\n')))))
def zad5():
    a=input('Podaj a\n')
    b=input('Podaj b\n')
    c=input('Podaj c\n')
    a=float(a)
    b=float(b)
    c=float(c)
    if 0<a<=10:
        print(str(a) +' należy do przedziału (0,10]')
    else:
        print('a nie należy do przedziału (0,10]')
    if a>b or b>c:
        print('Liczby spełniają drugi warunek, tzn nie są w kolejności rosnącej')
    else:
        print('Liczby nie spełniają drugiego warunku, tzn są w kolejności rosnącej')
def zad6():
    for x in range(5,100,5):
        print(x)
def zad7():
    for i in range(5):
        try:
            print('Kwadrat tej liczby to '+str(int(input('Podaj liczbę\n')) ** 2))
        except ValueError:
            print('Nie umiem podnosić liter do kwadratu')

def zad8():
    lista=list()
    a=input('Podaj liczbe do listy. Aby zakończyć wciśnij \'k\' \n')
    while a!='k':
        try:
            lista.append(float(a))
        except ValueError:
            print('To nie jest liczba')
        a=input('Podaj kolejną liczbę do listy \n')
    else:
        print(lista)
def zad9():
    a=input('Podaj liczbę\n')
    i=0
    suma=0
    while i < len(a):
        suma+=int(a[i])
        i+=1
    print(suma)
def zad10():
    for x in range(int(input('Podaj liczbę naturalną z przedziału [1,10]'))):
        print ('A'*(x+1))
def zad11():
    a=int(input('Podaj wysokość diamencika - liczbę nieparzystą z przedziału [3,9]\n'))
    srodek=int((a+1)/2)
    for x in range(1,a+1,1):
        print('{:^10}'.format('o'*(2*(srodek-abs(srodek-x))-1)))
def zad12():
    cyfry=list(range(1,11,1))
    print('  x  ', end='')
    for i in cyfry:
        print ('{:^5}'.format(cyfry[i-1]), end='')
    print('\n')
    for i in cyfry:
        print ('{:^5}'.format(i), end='')
        for j in cyfry:
            print ('{:^5}'.format(cyfry[j-1]*i), end='')
        print('\n')
def zad14():
    a=input('Proszę podać liczbę do liczenia pierwiastka\n')
    try:
        print('Pierwiastek z ' + a +' to ' +str(math.sqrt(int(a))))
    except ValueError:
        print('Niestety, ta funkcja nie liczy pierwiastków z liczb ujemnych')
def zad15():
    a=input('Podaj liczbę')
    i=0
    while i<len(a):
        try:
            int(a[i])
        except ValueError:
            print ("Halo, miała być liczba")
            break
        i+=1
    else:
        print("Dzieki")           

zad1()
zad2()
zad4()
zad5()
zad6()
zad7()
zad8()
zad9()
zad10()
zad11()
zad12()
zad14()
zad15()
