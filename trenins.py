def rezultats(sk1, sk2):
    if sk1<6 and sk2<6:
        rez = sk1*sk2
    else:
       rez = sk1+sk2

    return rez

for skaitlis in range(1,11, 2): #raange ir funkcija, kas skaita skaitļus
    for otrs in range(2, 11, 2):
      print("pirmais skaitlis:", skaitlis, "otrais skaitlis:", otrs, "rezultāts:", rezultats(skaitlis, otrs))


def zvaigznites(skaits):
   for rindasNr in range(1, skaits+1):
      for zvaigzne in range(rindasNr):
      print("*", end="")
      print("")

      zvaigznites2(skaits):
      

zvaigznites(5)

skaitlis1 = 7
skaitlis2 = 3


print("pirmais skaitlis:", skaitlis1)
print("otrais skaitlis:", skaitlis2)
print("rezultāts:", rezultats(skaitlis1,skaitlis2))