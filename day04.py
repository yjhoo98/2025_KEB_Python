#SOLID
#Open cloesd principle:개방 페쇄 원칙(확장에는 열려 있고 수정에는 닫혀있는 원칙)

def factorial_repetition(n)->int:
    result=1
    for i in range(2,n+1):
        result=result*i
    return result
number =int(input())
print(f"{number}!={factorial_repetition(number)}")
