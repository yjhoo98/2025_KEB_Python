def is_prime(num)->bool:
    """
    if num is prime number->return True/if num is not prime number->return False
    :param num:integer number
    :return:boolean type
    """

    if num >= 2:

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                # is_prime = False
                #break
                return False
            # print(i, end=' ')
    else:
        return False
    return True
n=int(input("Input Number:"))

if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")

