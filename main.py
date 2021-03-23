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
# print('zad4 \n')
# class NaZakupy:
#     nazwa_produktu = ''
#     ilosc = 0
#     jednostka_miary = ''
#     cena_jed = 0
#
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
#     def ile_produktu(self):
#         print(self.ilosc + ' ' + self.jednostka_miary)
#     def ile_kosztuje(self):
#         wynik = self.ilosc * self.cena_jed
#         return wynik


# zad5
# print('zad5 \n')
# class ciagi:
#     wyrazy = [3, 4, 5]
#     wyrazy_nowe2 = []
#     a = 0
#     # a1 = 0
#     # roznica = 0
#     # ilosc = 0
#
#     def wyswietl_dane(self):
#         print(self.wyrazy)
#     def pobierz_elementy(self, *a):
#         wyrazy_nowe = [x for x in a]
#         print(wyrazy_nowe)
#
#     def pobierz_parametry(self, a1, roznica, ilosc):
#         self.a1 = a1
#         self.roznica = roznica
#         self.ilosc = ilosc
#
#     def policz_sume(self, *a):
#         self.wyrazy_nowe2 = [x for x in a]
#         suma = 0
#         for x in self.wyrazy_nowe2:
#             suma = suma+x
#         print(suma)
#
#     def policz_elementy(self, *a):
#         wyrazy3 = [x for x in a]
#         print(len(wyrazy3))
#
#
# ciagi = ciagi()
# ciagi.wyswietl_dane()
# ciagi.pobierz_elementy(13, 15, 16, 18, 19)
# ciagi.pobierz_parametry(2, 2, 5)
# ciagi.policz_sume(5,10,20)
# ciagi.policz_elementy(6, 7, 8, 9, 0)


# zad6
# print('zad6 \n')
# class Robaczek:
#     x = 0
#     y = 0
#     krok = 1
#
#     def __init__(self, x = 0, y = 0, krok = 1):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def idz_w_gore(self, ile_krokow):
#         self.y += (ile_krokow * self.krok)
#
#     def idz_w_dol(self, ile_krokow):
#         self.y -= (ile_krokow * self.krok)
#
#     def idz_w_lewo(self, ile_krokow):
#         self.x -= (ile_krokow * self.krok)
#
#     def idz_w_prawo(self, ile_krokow):
#         self.x += (ile_krokow * self.krok)
#
#     def pokaz_gdzie_jestes(self):
#         print('(', self.x, ',', self.y, ')')
#
# robaczek = Robaczek()
# robaczek.idz_w_prawo(10)
# robaczek.idz_w_lewo(6)
# robaczek.idz_w_gore(5)
# robaczek.idz_w_dol(3)
# robaczek.pokaz_gdzie_jestes()










