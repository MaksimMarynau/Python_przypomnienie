"""
ZADANIE 2.10
Mamy dany napis wielowierszowy line. Podać sposób obliczenia liczby wyrazów w napisie. Przez wyraz rozumiemy
ciąg "czarnych" znaków, oddzielony od innych wyrazów białymi znakami (spacja, tabulacja, newline).
"""
print("___ZADANIE_2.10___")

with open('text.txt','r') as file:
    num_w = 0
    for line in file:
        num = len(line.split())
        num_w += num
        print("Number of words in line: ", num)
    print("Number of words in text: ", num_w)

"""
ZADANIE 2.11
Podać sposób wyświetlania napisu word tak, aby jego znaki były rozdzielone znakiem podkreślenia.
"""
print("___ZADANIE_2.11___")

print("_".join("word"))

"""
ZADANIE 2.12
Zbudować napis stworzony z pierwszych znaków wyrazów z wiersza line. Zbudować napis stworzony z ostatnich
znaków wyrazów z wiersza line.
"""
print("___ZADANIE_2.12___")
word_1 = ""
word_2 = ""
with open('text.txt','r') as file:
    for line in file:
        words = list(line.split(" "))
        print(words)
        for w in words:
            if w == "\n":
                continue
            else:
                word_1 += w[0]
                if w[len(w)-1] == "\n":
                    word_2 += w[len(w) - 2]
                else:
                    word_2 += w[len(w) - 1]

print(word_1)
print(word_2)


"""
ZADANIE 2.13
Znaleźć łączną długość wyrazów w napisie line. Wskazówka: można skorzystać z funkcji sum().
"""

print("___ZADANIE_2.13___")

with open('text.txt','r') as file:
    sum_chars = 0
    for line in file:
        list_of_words = line.split()
        for l in list_of_words:
            sum_chars += len(l)
print("Sum of chars in text: ", sum_chars)


"""
ZADANIE 2.14
Znaleźć: (a) najdłuższy wyraz, (b) długość najdłuższego wyrazu w napisie line.
"""

print("___ZADANIE_2.14___")

with open('text.txt','r') as file:
    max_len = 0
    word = ""
    for line in file:
        for w in line.split():
            if len(w) > max_len:
                word = w
                max_len = len(w)

print(f"The word with max chars: -->{word}<--, and length equal {len(word)}")

"""
ZADANIE 2.15
Na liście L znajdują się liczby całkowite dodatnie. Stworzyć napis będący ciągiem cyfr kolejnych liczb z listy L.
"""
print("___ZADANIE_2.15___")
L = list(range(50))
new_word = ""
for l in L:
    new_word += str(l)
print(new_word)

"""
ZADANIE 2.16
W tekście znajdującym się w zmiennej line zamienić ciąg znaków "GvR" na "Guido van Rossum".
"""
print("___ZADANIE_2.16___")
line = "Python is a widely used high-level GvR programming languageGvR  for geneGvRral-purpose programming."
line = line.replace("GvR","Guido van Rossum")
print(line)

"""
ZADANIE 2.17
Posortować wyrazy z napisu line raz alfabetycznie, a raz pod względem długości. Wskazówka: funkcja wbudowana
sorted().
"""
print("___ZADANIE_2.17___")
list_to_sort = line.split()
list_to_sort.sort(key=str.lower)
print(list_to_sort)
list_to_sort.sort(key=len)
print(list_to_sort)

"""
ZADANIE 2.18
Znaleźć liczbę cyfr zero w dużej liczbie całkowitej. Wskazówka: zamienić liczbę na napis.
"""
print("___ZADANIE_2.18___")
L = [1,2,0,50002,220,3003]
num = 0
for number in L:
    print(str(number).count('0'))
"""
ZADANIE 2.19

Na liście L mamy liczby jedno-, dwu- i trzycyfrowe dodatnie. Chcemy zbudować napis z trzycyfrowych bloków, gdzie
liczby jedno- i dwucyfrowe będą miały blok dopełniony zerami, np. 007, 024. Wskazówka: str.zfill().
"""
print("___ZADANIE_2.19___")
L = [1,2,7,402,220,503,3,9,2]
for num in L:
    print(str(num).zfill(3))