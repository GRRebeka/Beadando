
def Fibonacci_100():
    fib=[0,1]
    db=2
    i=1
    while db!=100:
        fib.append(fib[i-1]+fib[i])
        print(fib)
        db+=1
        i+=1
        print(db)

def main():
    Fibonacci_100()
main()