#1) for-> while
#2) while로 구간 소수를 출력
#3) **대신 pow함수
#4)**연산자, pow 함수를 사용하지 않고 커스텀 함수를 만들어 동작되도록 한다. my_pow
import math
def my_pow(num,i):
    """

    :param num:base number
    :param i:exponent
    :return:result
    """
    result = 1
    if i>=0:


        e = int(i)
        f = i - e

        for _ in range(e):  # for k in range(e):
            result = result * num

        if f > 0:
            result = result * math.exp(f * math.log(num))
        return result

    elif i<0:

            j=-i
            # while a<j:
            #     result=result/num
            #     a=a+1
            # return result
            e = int(j)
            f = j - e

            for _ in range(e):  # for k in range(e):
                result = result * num

            if f > 0:
                result = result * math.exp(f * math.log(num))

            return 1/result

def is_prime(num)->bool:
    """
    if num is prime number->return True/if num is not prime number->return False
    :param num:integer number
    :return:boolean type
    """
    if num >= 2:
        i=2
        while i<=int(my_pow(num,0.5)):
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
print(my_pow(2,-0.5))
number=input("숫자 두개 입력:").split(' ')
firstnum=int(number[0])
secondnum=int(number[1])

if firstnum>secondnum:
    firstnum,secondnum=secondnum,firstnum
cnt=firstnum
while cnt<=secondnum:
    if is_prime(cnt):

        print(f"{cnt}",end=' ')

    cnt=cnt+1
