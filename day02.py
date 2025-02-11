
n=int(input("Input Number:"))
is_prime=True
if n>=2:
    # count=0
    for i in range(2,int(n**0.5)+1):
        if n %i==0:
            # count=count+1
            is_prime=False
            break
        print(i,end=' ')
else:
    is_prime=False
if is_prime:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")

# dan =int(input("Input dan:"))
# for i in range(1,10):
#     print(f"{dan}*{i}={dan*i}")
# for dan in range(2,10):
#     for i in range(1,10):
#         print(f"{dan}*{i}={dan*i}")