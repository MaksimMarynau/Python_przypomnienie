"""
ZADANIE 4.2
Rozwiązania zadań 3.5 i 3.6 z poprzedniego zestawu zapisać w postaci funkcji, które zwracają pełny string przez return.
"""

print("--->ZADANIE 4.2<---")

length = int(input("Enter the length of measure: "))

def miarka(length):
    miarka = "|...."
    miarka = miarka * (length) + "|\n"
    for i in range(length + 1):
        if i == 0:
            miarka += str(i)
        else:
            miarka += "%5d" % (i)
    return miarka

print(miarka(length))


def square(size,size2):
    square = ""
    size = range(size)
    size2 = range(size2)
    for x in size:
        square += "+---"*len(size2)+"+\n"
        square += "|   "*(len(size2)+1)+"\n"
        if x == len(size)-1:
            square += "+---"*len(size2)+"+\n"
    return square
print(square(5,10))

"""
ZADANIE 4.3
Napisać iteracyjną wersję funkcji factorial(n) obliczającej silnię.
"""
print("--->ZADANIE 4.3<---")
def factorial(n):
    fact_tmp = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2,n+1):
            fact_tmp = fact_tmp*i
        return fact_tmp
print(factorial(5))

"""
ZADANIE 4.4
Napisać iteracyjną wersję funkcji fibonacci(n) obliczającej n-ty wyraz ciągu Fibonacciego.
"""
print("--->ZADANIE 4.4<---")

def fibonacci(n):
    if n == 0:
        return 0
    else:
        a = 0
        b = 1
        for i in range(1,n):
            tmp = a + b
            a = b
            b = tmp
        return b
print(fibonacci(9))

"""
ZADANIE 4.5
Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do right włącznie.
Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną.
"""
print("--->ZADANIE 4.5<---")
def iter_reverse(L, left, right):
    if right < left:
        left, right = right, left
    for i in range((right - left) // 2):
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def replace(L, left, right):
    L[left], L[right] = L[right], L[left]
    if left < right:
        return replace(L, left + 1, right - 1)
    else:
        return True


L = [1, 2, 3, 4, 5, 6, 7, 8]
left = 1
right = 5
print(L)
iter_reverse(L, left, right)
print(L)
replace(L, left, right)
print(L)

"""
ZADANIE 4.6
Napisać funkcję sum_seq(sequence) obliczającą sumę liczb zawartych w sekwencji, która może zawierać zagnieżdżone
podsekwencje. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie, czy element jest sekwencją, wykonać przez
isinstance(item, (list, tuple)).
"""
print("--->ZADANIE 4.6<---")
sequence = [(1, 2), 3, (6, [10, 12], (8, 1, (5, 4, 2)))]


def sum_seq(sequence):
    sum = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            sum += sum_seq(item)
        else:
            sum += item
    return sum

print(sum_seq(sequence))

"""
Mamy daną sekwencję, w której niektóre z elementów mogą okazać się podsekwencjami, a takie zagnieżdżenia mogą się
nakładać do nieograniczonej głębokości. Napisać funkcję flatten(sequence), która zwróci spłaszczoną listę wszystkich
elementów sekwencji. Wskazówka: rozważyć wersję rekurencyjną, a sprawdzanie czy element jest sekwencją, wykonać
przez isinstance(item, (list, tuple)).
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print flatten(seq) # [1,2,3,4,5,6,7,8,9]
"""
print("--->ZADANIE 4.7<---")

def flatten(sequence):
    L = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            L.extend(flatten(item))
        else:
            L.append(item)
    return L

sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print(flatten(sequence))
