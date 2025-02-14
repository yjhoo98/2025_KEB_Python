# def fibonacci_recursion(n):
#     """
#     fibonacci sequence using recurion
#     :param n:integer
#     :return:fibonacci sequence
#     """
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
# def fibonacci_repetition(n)->int:
#     n_list=[0,1]
#     for i in range(n+1):
#         n_list.append(n_list[i]+n_list[i+1])
#     return n_list[n]
# num=int(input("number:"))
# print(fibonacci_repetition(num))
# print(fibonacci_recursion(num))
def boom_repetition(n):

    for i in range(n,-1,-1):
        if i == 0:
            print(f"boom")
        elif i>0:
            print(f"{i}",end=" ")
def boom_recursion(n):
    if n<0:
        return
    elif n==0:
        print(f"boom")
    else:
        print(f'{n}',end=' ')
    return boom_recursion(n-1)
boom_repetition(int(input("num:")))
boom_recursion(int(input("num:")))