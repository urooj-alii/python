def mult(a,b):
    return a*b


def division(a,b):
    return a/b


def prime_num(a):
        for i in range(2,a):
            if a<2:
                 print("num is not prime")
            elif a%i==0:
                print(f"{a} is not prime")
                break
        else:
            print(f"{a} is prime")
    