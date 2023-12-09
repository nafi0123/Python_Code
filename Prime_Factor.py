def prime_factor(num):
    i=2
    while num>1:
        if num%i ==0:
            print(i,end=",")
            num=num//i
        else:
            i=i+1
            
inp=int(input())
prime_factor(inp)
