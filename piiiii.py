# PROSTE MATEMATYCZNE 
import math
# 1
# zadeklaruj funkcje oblicz_pole_kwadratu, która przyjmuje bok jako daną wejściową 
# funkcja ma zwracać wielkość pola kwadratu
def oblicz_pole_kwadratu(bok):
    return (bok ** 2)

# 2
# zadeklaruj funkcje oblicz_obwod_kwadratu, która przyjmuje bok jako daną wejściową
# funkcja ma zwracać wielkość obwodu kwadratu 
def oblicz_obwod_kwadratu(bok):
    return (4 * bok)


# 3 
# zadeklaruj funkcje oblicz_przeciwprostokatna, która przyjmuje dwie zmienne a i b 
# reprezentujące długość boków a i b
# funkcja ma zwracać długośc przeciwprostokątnej
# podpowiedź: importuj paczkę math i skorzystaj z funkcji math.sqrt()
# przykład użycia math.sqrt(4) --> 2
def oblicz_przeciwprostokatna(a,b):
    return math.sqrt(a*a + b*b)


# 4
# zadeklaruj funkcję oblicz_cale, która przyjmuje wartość liczbową centymetrów
# funkcja ma zwracać liczbę celi 
# przyjmij, że 1 cm = 0.39 cala
# rozwiązanie zaokrąglij do 2 miejsca po przecinku
# podpowiedź: użyj funkcji round(liczba, ilosc_miejsc_po_przecinku)
def oblicz_cale(cm):
    cale = cm*0.39
    return round(cale, 2)

# 5 
# zadeklaruj funkcję oblicz_brakujacy_kat_trojkata, który przyjmuje dwie wartości liczbowe 
# reprezentujące dwa kąty w trójkącie
# jeśli jest to możliwe zwróć wartość dla trzeciego kąta
# jeśli nie jest to możliwe zwróć 0 (zero)
def oblicz_brakujacy_kat_trojkata(kat1, kat2):
    if kat1 + kat2 < 180:
        return 180 - kat1- kat2
    else:
        return 0

# 6
# zadeklaruj funkcję oblicz_objetosc_szescianu, ktory przyjmuje dlugosc boku szescanu
# jako dana wejsciowa
# funkcja powinna zwracac wielkosc objetosci szescianu
def oblicz_objetosc_szescianu(bok):
    return (bok ** 3)
# 7 
# zadeklaruj funkcję czy_parzysta, która przyjmuje jako daną wejściową liczbę
# funkcja powinna zwrócić True dla wartości parzystej 
# i False dla wartości nieparzystej
def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

# 8
# zadeklaruj funkcję oblicz_sume_dwoch_wartosci_bezwglednych, która  
# przyjmuje dwie liczby, dodaje ich wartości bezwględne do siebie 
# funkcja powinna zwrócić wynik dodawania
# Przykład: |-2| + |2| = 4
# Przykład 2: |0| + |-7| = 7
# Przykład 3: |-10| + |-10| = 20
# Przykład 4: |10| + |10| = 20
def oblicz_sume_dwoch_wartosci_bezwglednych(liczba1, liczba2):
    return abs(liczba1) + abs(liczba2)
    

# STREFA SKRYPTU
if __name__ == '__main__':
    print("Tutaj wywołuj funckje")
    print(oblicz_pole_kwadratu(4))
    print(oblicz_objetosc_szescianu(4))

# ŁAŃCUCHY ZNAKÓW

# 1
# Zadeklaruj funkcję wymien_slowa_po_przecinku, ktora przyjmuje łańcuch znaków 
# funkcja ma zwrócić łańcuch znaków, którego słowa orginalnego łańcucha zostały
# podzielone przecinkiem, jak w przykładzie poniżej:
# Przykład: "tosty ser szynka" --> "tosty, ser, szynka"
def wymien_slowa_po_przecinku(text):
    return ','.join(text.split())

# 2 
# Napisz funkcję odwroc_litery, która przyjmuje ciąg liter i małe zamienia na duże, 
# zaś duże na małe 
# Przykład "HeLLo" ---> "hEllO"
# Podpowiedź: żeby stwierdzić, czy litera jest duża, czy mała możesz wykorzystać 
# metodę łańcucha znaków: isupper()
# Przykład użycia: "a".isupper() --> False
# Podpowiedź 2: żeby sprawić, aby litery zmianiły swoją wielkość użyj metody 
# upper() lub lower()
def odwroc_litery(text):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in text])

# 3
# Napisz funkcję cenzuruj, która przyjmuje ciąg znaków
# Funkcja ma zwracać ocenzurowany ciąg znaków
# wyrazy: Python ma być wygwiazdkowany
# Przykład: "Moim ulubionym językiem programowania jest Python" -->
# "Moim ulubionym językiem programowania jest ******"
def cenzuruj(text):
    return text.replace('Python', '******')

# 4 
# Napisz funkcję formatuj_date, która przyjmuje ciąg znaków oznaczający datę
# w formacie amerykańckim MM/DD/YYYY, a zwraca w formacie polskim DD.MM.YYYY r.
# Przykład: "02/10/2010" --> "10.02.2010 r."
def formatuj_date(text):
    miesiac, dzien, rok = text.split('/')
    return f"{dzien}.{miesiac}.{rok} r."

# 5 
# Napisz funkcje usun_polskie_znaki, która przyjmuje ciąg liter
# Funcja ma zwracać ciąg, który został transliterowany
# Pozbadź się ogonków
# Przykład: "żółć" --> "zolc"
# ą --> a
# ć --> c
# ę --> e
# ł --> l
# ń --> n
# ó --> o
# ś --> s
# ź --> z
# ż --> z
def usun_polskie_znaki(text):
    polskie_znaki = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś':'s', 'ź': 'z', 'ż': 'z'}
    return ''.join([polskie_znaki.get(char, char) for char in text])

# STREFA SKRYPTU
if __name__ == '__main__':
    print("Tutaj wywołuj funkcje")
    print(wymien_slowa_po_przecinku("tosty ser szynka"))
    print(odwroc_litery("HeLLo"))
    print(cenzuruj("Moim ulubionym językiem programowania jest Python"))
    print(formatuj_date('02/10/2010'))
    print(usun_polskie_znaki('żółć'))

# TABLICE

# 1
# Napisz funckję oblicz_sume_w_kolumnach, która przyjmuje tablice tablic 
# i zlicza sume w kolumnach
# Przykład: 
# [[1,2,3,4,5],
#  [8,3,2,1,5]] --> [9,5,5,5,10]
# Tablica może mieć dwolną licznę kolumn i wierszy
def oblicz_sume_w_kolumnach(tablica):
    kolumny = len(tablica[0])
    suma_kolumn = [0] * kolumny
    for wiersz in tablica:
        for i in range(kolumny):
            suma_kolumn[i] += wiersz[i]
    return suma_kolumn

# 2
# Napisz funkcję usun_duplikaty_z_listy, usuwającą duplikaty z listy
# Funkcja ma przyjmować tablice 
# Funkcja ma zwracać tablicę bez duplikatów
# Przykład: ['kot', 'kot', 'pies'] --> ['kot', 'pies']
# Przykład 2: [1,2,3,3,4] --> [1,2,3,4]
def usun_duplikaty_z_listy(tablica):
    return list(set(tablica))


# 3
# Napisz funckję znajdz_wspolne_elementy, która przyjmuje dwie listy jako wejście 
# Funkcja ma zwracać listę wspólnych elementów
# Przykład: ['kot', 'pies'], ['krolik', 'kaczka'] --> []
# Przykład 2: ['kot', 'pies'], ['kot', 'kaczka'] --> ['kot']
def znajdz_wspolne_elementy(lista1, lista2):
    return list(set(lista1) & set(lista2))

# 4 
# Napisz funkcję znajdz_drugi_najwiekszy_element, która przyjmuje tablice
# Funkcja ma zwracać drugą największą w tablicy wartość
# Przykład: [1,2,3,4,5,6] --> 5
# Przykład 2: [4,5,8,1,3,9] --> 8
def znajdz_drugi_najwiekszy_element(tablica):
    unikalne = list(set(tablica))
    unikalne.sort(reverse=True)
    return unikalne[1] if len(unikalne) > 1 else None

# 5 
# Funkcja znajdz_brakujaca_liczbe, która przyjmuje jako daną wejściową tablicę.
# Przykład:
# [[1,   2, 1, 4], 
#  ['x', 3, 3, 2],
#  [2,   4, 4, 3], 
#  [3,   1, 2, 1]] --> 4
# W każdej kolumnie musi znaleźć się liczba od 1 do 4. 
# Funkcja ma zwracać wartość x
# Podpowiedź: x jest łańcuchem znaków.
# żeby sprawdzić, jakiego typu jest element możesz użyć funkcji type()
# Przykład użycia: type(7) == str --> False, bo 7 nie jest typu string 
def znajdz_brakujaca_liczbe(tablica):
    for kolumna in range(len(tablica[0])):
        liczby = set()
        for wiersz in tablica:
            if type(wiersz[kolumna]) == int:
                liczby.add(wiersz[kolumna])
        for liczba in range(1, 5):
            if liczba not in liczby:
                return liczba
    return None


# STREFA SKRYPTU
if __name__ == '__main__':
    print("Tutaj wywołuj funckje")
    print(oblicz_sume_w_kolumnach([[1,2,3], [3,2,1]]))
    print(usun_duplikaty_z_listy(['pies', 'pies', 'kot']))
    print(znajdz_wspolne_elementy(['kot', 'pies'], ['kot', 'kaczka']))
    print(znajdz_drugi_najwiekszy_element([1,2,3,4,9,5]))
    print(type('x'))
    print(znajdz_brakujaca_liczbe([[1,   2, 1, 4], 
                                    ['x', 3, 3, 2],
                                    [2,   4, 4, 3], 
                                    [3,   1, 2, 1]]))
    print(znajdz_brakujaca_liczbe([[1,   2, 1, 4], 
                                    [4, 'x', 3, 2],
                                    [2,   4, 4, 3], 
                                    [3,   1, 2, 1]]))

# ZŁOŻONE
import math
# 1
# Napisz funckję zwroc_schody, która przyjmuje liczbę schodów
# i zwraca tablicę schodów o określonej podstawie
# Przykład: 4
#    # (trzy spacje, jeden hash)
#   ## (dwie spacje, dwa hashe)
#  ### (jedna spacje, trzy hashe)
# #### (cztery hashe)
# Oczekiwany wynik: ['   #', '  ##', ' ###', '####']
# Zauważ, że liczba elementów tablicy jest równa liczbie wejściowej
# Zaś liczba znaków w elemencie także jest równa liczbie wejściowej
# Podpowiedź: aby przejść określoną ilość razy przez pętle możesz
# wykorzystać generator range(x), który wygeneruje wartości od 0 do x-1
# Podpowiedź 2: generator range może przyjąć także wartość początkową 
# i końcową np. range(1, x+1) --> 1, 2 , ..., x
def zwroc_schody(n):
    return [f"{' ' * (n - i - 1)}{'#' * (i + 1)}" for i in range(n)]

# 2
# Napisz funckję oblicz_procent_z_wartosci, która przyjmuje ciąg znaków i liczbę 
# następnie konwertuj ciąg reprezentujący wartość procentową na liczbę
# i dokonaj obliczeń 
# Przykład: "10%", 200 --> 0.1 * 200 --> 20
# wynik podaj zaaokrąglony do 2 miejsca po przecinku
# Podpowiedź: możesz wykorzystać funckję round(liczba, ilosc_miejsc_po_przecinku)
def oblicz_procent_z_wartosci(procent, wartosc):
    procent = float(procent.strip('%')) / 100
    wynik = procent * wartosc
    return round(wynik, 2)


# 3 
# Napisz funckję oblicz_dlugosc_prostej, która przyjmuje dwie dane wejściowej:
# punkt A i punkt B zapisany w formacie [x, y] oznaczający punkt na osi współrzędnych.
# Następnie oblicz długośc odcinka między punktami.
# Podpowiedź: wzór na długośc odcinka to
# |AB|=√((x2−x1)^2+(y2−y1)^2) 
# Podpowiedź: importuj paczkę math i skorzystaj z funkcji math.sqrt()
# przykład użycia math.sqrt(4) --> 2
# wynik zaokrąglij do 2 miejsca po przecinku
# Podpowiedź: możesz wykorzystać funckję round(liczba, ilosc_miejsc_po_przecinku)
# Podpowiedź: do obliczenia wartości bezględnej użyj funckji np. abs(-10) --> 10
def oblicz_dlugosc_prostej(A, B):
    x1, y1 = A
    x2, y2 = B
    dlugosc = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(dlugosc, 2)

# 4 
# Napisz funckję oblicz_ilosc_wyrazow, która przyjmuje ciąg słów, 
# Funkcja ma zwracać liczbę słów w ciągu w tablicy w formacie: [słowo, liczba_wystąpień]
# Przykład: 'ala kot kot kot ala pies' --> [['ala', 2], ['kot', 3], ['pies', 1]]
def oblicz_ilosc_wyrazow(text):
    wyrazy = text.split()
    licznik = {}
    for wyraz in wyrazy:
        licznik[wyraz] = licznik.get(wyraz, 0) + 1
    return [[wyraz, liczba] for wyraz, liczba in licznik.items()]


# STREFA SKRYPTU
if __name__ == '__main__':
    print("Tutaj wywołuj funckje")
    print(zwroc_schody(7))
    print(oblicz_procent_z_wartosci('10%', 200))
    print(oblicz_dlugosc_prostej([1,2], [3,7]))
    print(oblicz_ilosc_wyrazow('ala kot kot kot ala pies Ala'))
