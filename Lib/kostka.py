import random
print ('Podaj liczbę ścian kostki: ', end='')
kostka = int(input())
inp = 'y'
while inp == 'y':
    wynik = random.randint(1, kostka)
    print ('Wylosowałeś: ', wynik)
    print('Jeszcze raz? (y/n) ', end='')
    inp = input()