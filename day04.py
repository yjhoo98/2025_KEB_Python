#이중 decorator 적용/성능측정/discription/factorial

def log_decorator(func):
    def wrapper(*args,**kwargs):
        print(f"Function Name:{func.__name__}")
        print(f"Function Arguements:{args}")
        print(f"Function Keyword Arguements:{kwargs}")
        result=func(*args,**kwargs)
        return result
    return wrapper



def descript_func(func):
    def inner_desc(*args):
        print(func.__name__)
        print(func.__doc__)
        r = func(*args)
        return r
    return inner_desc
@log_decorator
def greet(name,greeting="안녕하세요",age=None):
    return f"{greeting},{name},(age{age})"if age else f"{greeting},{name}"
print(greet("인하"))
print(greet("인상","안녕"))
print(greet("James","HELLO"))
print(greet("Gonzales",greeting="Hola"))
print(greet("Nakamura",greeting="Gonniziwa",age=29))