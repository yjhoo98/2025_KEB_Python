#이중 decorator 적용/성능측정/discription/factorial
import time
def descript_func(func):
    def inner_desc(*args):
        print(func.__name__)
        print(func.__doc__)
        r = func(*args)
        return r
    return inner_desc

def time_decorator(func):

    def wrapper(*arg):
        s=time.time()
        r=func(*arg)
        e=time.time()
        print(f"{e-s}초 소요")
        return r
    return wrapper

# @time_decorator
# @descript_func
def factorial_repetition(n)->int:
    """

    :param n:integer number
    :return:n!
    """
    result=1
    for i in range(2,n+1):
        result=result*i
    return result
number =int(input())
# s=time.time()
t=descript_func(time_decorator(factorial_repetition))
print(f"{number}!={t(number)}")
# e=time.time()
# print(e-s)

