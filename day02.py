#1) for-> while
#2) while로 구간 소수를 출력
#3) **대신 pow함수
def is_prime(num)->bool:
    """
    if num is prime number->return True/if num is not prime number->return False
    :param num:integer number
    :return:boolean type
    """
    if num >= 2:
        i=2
        while i<=int(num**0.5):
            if num % i == 0:

                return False
            else:
                i=i+1
    else:
        return False
    # if num >= 2:
    #
    #     for i in range(2, int(num ** 0.5) + 1):
    #         if num % i == 0:
    #             # is_prime = False
    #             #break
    #             return False
    #         # print(i, end=' ')
    # else:
    #     return False
    return True
# n=int(input("Input Number:"))
#
# if is_prime(n):
#     print(f"{n} is prime number")
# else:
#     print(f"{n} is not prime number")

firstnum=int(input("Input First Number:"))
secondnum=int(input("Input Second Number:"))
cnt=firstnum
prime=[]
index=0
while cnt<=secondnum:
    if is_prime(cnt):
        print(f"{cnt}")
    cnt=cnt+1
