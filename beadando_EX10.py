
###2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? ###
###A 2520 a legkisebb szám, amely minden szám nélkül eloszlatható 1-től 10-ig. Mi a legkisebb pozitív szám, amely egyenlően osztható az összes 1-től 20-ig terjedő számra?###

import time

def osztas():
    db=0
    szam = 10
    while db!=10:
        for i in range(1,10):
            if szam%i==0:
                db+=1
        if db==10:
            return szam
        szam+=1
    print(szam)
    print(db)



osztas()




