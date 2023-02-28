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
            while(s[i][j]==0 and len(valin)<9):

                k=randomizza(valin)

                if control(k,i,j):
                    s[i][j]=k
                else:
                    valin.append(k)


            if len(valin)==9:
                svuota_riga(i)
                i-=1
                valin=[]
            j+=1
        i+=1
        j=0

riempi()
for i in range(9):
    print (s[i][0],s[i][1],s[i][2],s[i][3],s[i][4],s[i][5],s[i][6],s[i][7],s[i][8])
