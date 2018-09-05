
lst = [12, 544, 3, 55, 47, 43, 54, 541, 4441, 843]

def isPrime(n):
    flag=1
    if(n>1):
        for i in range(2,n):
        
            if(n%i==0):
                flag=0
                break
        if(flag==1):
            return n

for i in range(1, 100): 
     n = list(filter(lambda x: isPrime(x), lst))

print('Prime Numbers: ',n)


