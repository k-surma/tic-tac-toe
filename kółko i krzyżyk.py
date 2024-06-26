#tictactoe
import random
def Plansza(P):
    print("-"*7)
    for i in range(3):
        for j in range(3):
            print(f"|{P[i][j]}",end='')
        print("|")
        print("-"*7)

def Wybor_gracza():
    p={'O','X'}
    global pl
    pl=input("Wybierz kim jesteś (O/X): ")
    while pl not in p:
        pl=input("Wybierz O lub X!: ")
    print("Wybrałeś: ",pl)
    Plansza([[1,2,3],[4,5,6],[7,8,9]])


def check_wygrana(w,c):
    if w[0][0]==w[1][1]==w[2][2]!=" " or w[0][2]==w[1][1]==w[2][0]!=" ":
        print("GRATULACJE! Wygrał gracz: ", c)
        return True
    elif any(((w[i][0] == w[i][1] == w[i][2] != " ") or (w[0][i] == w[1][i] == w[2][i] != " ")) for i in range(3)):
        print("GRATULACJE! Wygrał gracz: ", c)
        return True
    elif all(w[i][j] != " " for i in range(3) for j in range(3)):
        print("REMIS!")
        return True
    else:
        return False

def Ruch():
    z = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print("Podaj liczbe 1-9, aby wykonac ruch")
    global k
    k=pl
    while 1:
        try:
            j=False
            while not j:
                n=int(input(f"Kolej {k}: "))
                if n in range(1,10):
                    if z[(n-1)//3][(n-1)%3]!=" ":
                        print("To pole jest już zajęte!")
                    else:
                        z[(n - 1) // 3][(n - 1) % 3]=k
                        Plansza(z)
                        j=True

                else:
                    print("Niepoprawna liczba")
        except ValueError:
            print("Niepoprawny znak")
        if check_wygrana(z,k):
            break
        # zmiana gracza
        if k == "O":
            k = "X"
        elif k == "X":
            k = "O"

        #rozgrywka z komputerem
        if tr:
            komp = random.randint(1, 9)
            while z[(komp - 1) // 3][(komp - 1) % 3] != " ":
                komp = random.randint(1, 9)
            else:
                z[(komp - 1) // 3][(komp - 1) % 3] = k
            print(f"Kolej {k} (komputera): ")
            Plansza(z)
            if check_wygrana(z, k):
                break
            if k == "O":
                k = "X"
            elif k == "X":
                k = "O"

def tryb_gry():
    global tr
    while 1:
        n = int(input("Wybierz tryb gry. Wybierz: 1-rozgrywka z drugim graczem, 2-rozgrywka z komputerem: "))
        Wybor_gracza()
        if n==1:
            tr=False
        elif n==2:
            tr=True
        else:
            print("Wybierz opcję 1 lub 2")
        Ruch()

tryb_gry()