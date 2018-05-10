
###2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? ###

def osztas_10():      
    db=0
    szam = 10
    while db!=10:
        for i in range(1,11):
            if szam%i==0:
                db+=1
        if db==10:
            return szam
        else:
            db=0
        szam+=1



def osztas_20():
    db=0
    szam = 20
    while db!=20:
        if szam%20==0:
            db=1
            for i in range(1,20):
                if szam%i==0:
                    db+=1
        if db==20:
            return szam
        else:
            db=0
        szam+=20
    return szam


print(osztas_10())
print(osztas_20())

