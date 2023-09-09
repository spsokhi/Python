n=int(input("Enter num to check it's prime or not :"))
prime=0
if(n>1):
    for i in range(2,n):
        if(n%i==0):
            prime=1
            break
else:
    print("The number should be greater than 1 ")
if(prime==1):
    print(n,"Is not a prime number")
else:
    print(n,"Is a prime number")
