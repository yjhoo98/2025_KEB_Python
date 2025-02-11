n=int(input("Input Number:"))
count=0
for i in range(1,n+1):
    if n %i==0:
        count=count+1
if count==2:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")

# dan =int(input("Input dan:"))
# for i in range(1,10):
#     print(f"{dan}*{i}={dan*i}")
# for dan in range(2,10):
#     for i in range(1,10):
#         print(f"{dan}*{i}={dan*i}")