def my_abs(n)->int:
    """
    Return Absolute value of parameter n
    :param n:
    :return: absolute value
    """
    if n<0:
        return-n
    return n
def my_fibonacci_recursion(n):
    """
    fibonacci sequence using recurion
    :param n:integer
    :return:fibonacci sequence
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return my_fibonacci_recursion(n-1)+my_fibonacci_recursion(n-2)