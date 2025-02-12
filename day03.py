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

print(my_pow(10,-2))