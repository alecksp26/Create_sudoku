from random import randint

s=[ [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0]
   ]
sudoku=[ [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]
          ]


def control_column(k,j) :
    for i in range (0,9):
        if k== s[i][j]:
            return False
    return True
def control_row(k,j):
    for i in range (0,9):
        if k== s[j][i]:
            return False
    return True
def control_tab(k,i,j):

    if i<3:

        tr=0

    elif i<6 and i>=3:

        tr=3

    elif i>=6:

        tr=6

    if j<3:

        tc=0

    elif j<6 and j>=3:

        tc=3

    elif j>=6:

        tc=6

    for l in range (tr,tr+3):

        for m in range (tc,tc+3):

            if k==s[l][m]:

                return False

    return True
def control(k,i,j):

    if control_column(k,j) and control_row(k,i)and control_tab(k,i,j):

        return True

    return False

def svuota_riga(i):

    for j in range(9):

        s[i][j]=0

def check(i,valin):

    for j in range(len(valin)):

        if i==valin[j]:

            return True

    return False

def randomizza(valin):

    randomizzabili=[]

    for i in range(1,10):

        if check(i,valin):

            continue

        else:

            randomizzabili.append(i)

    k=randint(0,len(randomizzabili)-1)

    return randomizzabili[k]
def riempi():

    valin=[]
    i=0
    j=0
    while(i<9):
        while (j<9):
            valin=[]
            while(s[i][j]==0 and len(valin)<9):



                k=randomizza(valin)

                if control(k,i,j):

                    s[i][j]=k
                else:

                    valin.append(k)


            if len(valin)==9:
                svuota_riga(i)
                svuota_riga(i-1)
                i-=2
                valin=[]
            j+=1
        i+=1
        j=0
def tabella_sudoku():


    riempi()
    for k in range (13):
        j=randint(0,3)
        i=randint(0,3)
        sudoku[i][j]=s[i][j]
        sudoku[8-i][8-j]=s[8-i][8-j]
def gioco():
    inn=100
    while(inn!=0):
        inn=int(input("metti un numero,0 se vuoi terminare"))
        i=int(input("metti riga"))
        j=int(input("metti colonna"))
        i=i-1
        j=j-1
        if inn==s[i][j]:
            sudoku[i][j]=inn
            print_game()
        else:
            print("errore")
def print_game():
   for i in range(9):
        print ("|",sudoku[i][0],sudoku[i][1],sudoku[i][2],sudoku[i][3],sudoku[i][4],sudoku[i][5],sudoku[i][6],sudoku[i][7],sudoku[i][8])
tabella_sudoku()
print_game()

gioco()
