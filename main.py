# zad1
# print('zad1 \n')
#
# liczby = []
# for x in range(0,31,1):
#     liczby.append(x)
# print(liczby)
# liczby2 = []
# for x in liczby:
#     liczby2.append(x*2)
# print(liczby2)
#
# plik = open('plik.txt','w')
# plik.write(str(liczby2))
# plik.close()


# zad2
# print('zad2 \n')
#
# plik = open('plik.txt','r')
# wiersze = plik.readlines()
# print(wiersze)
# plik.close()


# zad3
# print('zad3 \n')
#
# with open('text.txt', 'w') as plik:
#     plik.write('to jest linika 1\n')
#     plik.write('to jest jakas linika 2\n')
#     plik.write('to jest kolejna linika w tym pliku\n')
#
# with open('text.txt', 'r') as plik:
#     for x in plik:
#         print(x, end='')


# zad4
print('zad4 \n')
class NaZakupy:
    nazwa_produktu = ''
    ilosc = 0
    jednostka_miary = ''
    cena_jed = 0

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc + ' ' + self.jednostka_miary)
    def ile_kosztuje(self):
        wynik = self.ilosc * self.cena_jed
        return wynik


