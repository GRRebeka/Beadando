
###2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? ###

def osztas():
    db=0
    szam = 20
    while db!=20:
        for i in range(1,21):
            if szam%i==0:
                db+=1
        if db==20:
            return szam
        else:
            db=0
        szam+=1

def main():
    print(osztas())

main()


