"""
ZADANIE 3.1
Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?
"""
"""
Nie, bo sa pewne bledny dot. zbednych srednikow na koncu kodu, 
nie poprawna skladnia petli oraz w konsturkcji warunkowej
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

for i in "qwerty": if ord(i) < 100: print (i)
for i in "axby": print (ord(i) if ord(i) < 100 else i)

Prawidlowa wersja powyzszego kodu jest niżej napisana.
"""
print("--->ZADANIE 3.1<---")

x = 2; y = 3
if(x > y):
    result = x
else:
    result = y
print(result)

[print(i) for i in "qwerty" if ord(i) < 100]
[print(ord(i)) if ord(i) < 100 else print(i) for i in "axby"]

"""
Co jest złego w kodzie:
1)L = [3, 5, 4] ; L = L.sort()
Zbędne przypisywanie do zmiennej sortowanie listy( działanie jest IN PLACE )
2)x, y = 1, 2, 3
za duzo wartosci do pszypisania
3)X = 1, 2, 3 ; X[1] = 4
krotki sa immutable
4)X = [1, 2, 3] ; X[3] = 4
nie ma pozycji 3 na liscie. Odliczanie jest od zera.
5)X = "abc" ; X.append("d")
'STR' immutable i nie posiada takiej funkcji .append().
6)L = list(map(pow, range(8)))
Funkcja pow() wymaga dwa argumenty, podan jeden tylko.
"""
print("--->ZADANIE 3.2<---")


"""
ZADANIE 3.3
Wypisać w pętli liczby od 0 do 30 z wyjątkiem liczb podzielnych przez 3.
"""
print("--->ZADANIE 3.3<---")

for i in range(30):
    if i % 3 == 0:
        continue
    print(i, end=" ")

"""
ZADANIE 3.4
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący parę x i trzecią potęgę
x. Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to
program ma wypisać komunikat o błędzie i kontynuować pracę.
"""

print("--->ZADANIE 3.4<---")

while True:
    try:
        flt = input("Enter a float number: ")
        if flt == "stop":
            break
        else:
            flt = float(flt)
            print(flt, pow(flt, 3))
    except:
        print("Entered a string, program continuation...")
        continue

"""
ZADANIE 3.5
Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające się z kilku cyfr
(ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować pełny string, a potem go
wypisać.
"""
print("--->ZADANIE 3.5<---")

length = int(input("Enter the length of measure: "))
miarka = "|...."
miarka = miarka * (length) + "|\n"

for i in range(length+1):
    if i == 0:
        miarka += str(i)
    else:
        miarka += "%5d" % (i)
print(miarka)

"""
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string, a potem go wypisać.
Przykładowy prostokąt składający się 2x4 pól ma postać:
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
"""
print("--->ZADANIE 3.6<---")

square = ""
size = range(2)
size2 = range(4)
for x in size:
    square += "+---"*len(size2)+"+\n"
    square += "|   "*(len(size2)+1)+"\n"
    if x == len(size)-1:
        square += "+---"*len(size2)+"+\n"
print(square)

"""
Podany fragment programu pokaże problem z wyświetlaniem list obiektów stworzonych przez użytkownika, jeżeli nie
została zdefiniowana metoda __repr__. Jeżeli zdefiniowano tylko metodę __repr__, to zostanie ona użyta również wtedy,
gdy zwykle pracuje __str__. Sprawdzić działanie kodu, jeżeli wykomentujemy metodę __str__() lub metodę __repr__().
"""
print("--->ZADANIE 3.7<---")

class Time:
    def __init__(self, seconds=0):
        self.s = seconds
    def __str__(self):
        return "{} sec".format(self.s)
    def __repr__(self):
        return "Time({})".format(self.s)

time1 = Time(12)
time2 = Time(3456)
print(time1, time2) # Python wywołuje str()
print([time1, time2]) # Python wywołuje repr()

"""
ZADANIE 3.8
Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń), (b)
listę wszystkich elementów z obu sekwencji (bez powtórzeń).
"""
print("--->ZADANIE 3.8<---")

a = [[4, 5, 9], (13, 2), [3, 4], (5, 6, 7)]
b = [(0, 5, 1, 9), (3, 4), (5, 67, 7)]
new_a = set()
new_b = set()

for i in a:
    new_a.update(set(i))

for i in b:
    new_b.update(set(i))

print(new_a.intersection(new_b))
print(new_a.union(new_b))

"""
ZADANIE 3.9
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby. Znaleźć listę zawierającą sumy liczb z
tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)], spodziewany wynik [0,4,3,7,18].
"""

print("--->ZADANIE 3.9<---")

L = [[],[4],(1,2),[3,4],(5,6,7)]
print(list(map(lambda x: sum(x), L)))
"""
ZADANIE 3.10
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
(podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""

print("--->ZADANIE 3.10<---")


book_dict = dict( I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000 )

def roman_symbols():
    while True:
        try:
            book = input().upper()
            result = 0
            for i, c in enumerate(book):
                if i+1 < len(book) and book_dict[book[i]] < book_dict[book[i+1]]:
                    result -= book_dict[book[i]]
                else:
                    result += book_dict[book[i]]
            return print(result)
        except:
            print('We don\'t have this symbol. Try again...')
            continue

list_of_symbols = list('IVXLCDM')
print('Try to translate Romans symbol for Arabic numeral.\n'
      f'Write a symbol from list would you like to translate.\n{list_of_symbols}\n'
      f'You can also combine symbols. For example: XII , XIIM , XIIX , MCXVI...')
roman_symbols()