
###The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?###

def prim_e(szam):
    db=1
    if szam==2:
            return 'Prim'
    for i in range(2,szam):
        if szam%i == 0:
            db+=1
            if db>2:
                return 'Nem prim'
    return 'Prim'

def EX9(number):

    max=0
    for i in range(2,number):
        if number%i==0:
            if prim_e(i)=='Prim':
                if i>max:
                    max=i       
    print('{} the largest prim'.format(max))

EX9(600851475143)

