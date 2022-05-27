from ast import While
from ctypes import sizeof
from math import ceil
import random
from turtle import pd
import time
#---------------------Method for printing arrays ------------------------------
def arrayPrint(matrix):
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('-----------------------------------------------------------------')
    print('\n'.join(table))
    print('-----------------------------------------------------------------')
#---------------Implementation of Recursive -------------------------
def recurit(i,j):
    #------------Base Case---------
    #print("Called")
    if i == j:
        result = val[i]
        return result
    if j == i+1:
        result = max(val[i],val[j])
        return result
    #-----Recursive Algorithim----    
    result = max(val[i] + min(recurit(i+2,j), recurit(i+1,j-1)), val[j] + min(recurit(i+1,j-1),recurit(i,j-2)))
    print(result)
#-----------------Implementation of Dynamic Programming -----------------              
def timber(n,val):
#------- Build the table ---------------------
    T = [[0 for x in range(n)] for y in range(n)]
    TB = [[0 for x in range(n)] for y in range(n)] 
    
#------ Fill Table with base cases-------------
    for i in range(n-1,-1,-1):
        for j in range(n):
            if j >= i:
                if j == i:
                    T[i][j] = val[i]
                if j == i+1:
                    T[i][j] = max(val[i],val[j])  
#---------Calculte remaining items ------------      
    sel = []
    stringsel = []
    for i in range(n,-1,-1):
        for j in range(n):
            if j >= i and T[i][j] == 0:
                
                T[i][j] = max(val[i] + min(T[i+2][j], T[i+1][j-1]), val[j] + min(T[i+1][j-1],T[i][j-2]))
                
                #------ Logic For Filling Traceback Table ---------
                ii = val[i] + T[i+2][j]
                ij = val[i] + T[i+1][j-1]
                ji = val[j] + T[i+1][j-1]
                jj = val[j]+ T[i][j-2]

                if min(ii,ij)>min(jj,ji):
                    if ii>ij:
                        TB[i][j] = "ll"
                    else:
                        TB[i][j] = "lr"
                else:
                    if jj>ji:
                        TB[i][j] = "rr"
                    else:
                        TB[i][j] = "rl"
    i = 0
    j = n - 1
    
    while i < j:
        if TB[i][j] == "ll":
            sel.append(i+1)
            #val.pop(i+1)
            i = i+1
            sel.append(i+1)
            #val.pop(i+1)
            i = i+1
            stringsel.append("ll")
        elif TB[i][j] == "lr":    #Changed tp lr
            sel.append(i+1)    
            #val.pop(i+1)
            i = i +1
            sel.append(j+1) 
            #val.pop(len(val)-1)
            stringsel.append("lr")
            j = j - 1
        elif TB[i][j] == "rr":    #Changed to rr
            sel.append(j+1)
            #val.pop(len(val)-1)
            j = j - 1
            sel.append(j+1)
            #val.pop(len(val)-1)
            stringsel.append("rr")
            j = j-1
        elif TB[i][j] == "rl":    #Changed to rl
            sel.append(j+1)
            #val.pop(len(val)-1)
            j = j - 1
            sel.append(i+1)
            #val.pop(i+1)
            stringsel.append("rl")
            i = i+1
        elif TB[i][j] == "l":     #Changed to l
            sel.append(i+1)
            #val.pop(i+1)
            i = i+1
            stringsel.append("l")
        elif TB[i][j] == "r":     #aChanged to r
            sel.append(j+1)
            #val.pop(len(val)-1)
            j = j-1
            stringsel.append("r")
        else:
            #break
            sel.append(i-1)
            i= i+1
    summation = sum(range(1,n+1)) # What we should get
    zipper = sum(sel) #What we actually get
    missing = summation - zipper
    print(T[0][n-1])
    if missing > 0:
        sel.append(missing)
    print(sel)
    print(stringsel)

#------------------This is used for building the "tree"---------------
n = int(input("Enter the number of segments on the tree(n)\n"))
n = 20
mor = input("Do you want to fill your tree with manual or random values (m/r):\n")
    #manual
val=[]
lookback = []
rat = 0
if mor == 'r':
    val = [33, 28, 35, 23, 23, 25, 37, 40, 42, 24, 38, 29, 22, 40, 36, 42, 39, 37, 45, 32]
    #while rat<n:
    #    val.append(random.randint(1,100))
    #    rat=rat+1
elif mor == 'm':
    while rat<n:
        userInt = int(input("Enter value for the %s segment" %(rat+1)))
        val.append(userInt)
        rat=rat+1
else:
    print("Invalid input")
    exit()
print("Here is your tree:", val)
#---------------------------------------------------------------------------
#----------DP //comment out if unwanted -------
timber(n,val)
#---- Recursive //comment out if unwanted------
#i = 0
#j = n-1
#result = recurit(i,j)
#print("Recursive ", result)
#------------------ The End ---------------------
