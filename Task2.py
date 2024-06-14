from time import time

def external(param,):  
    def deco(func):
        def wrapper(*args):
            sum_time = 0
            for _ in range(param):
                t1 = time()
                res = func(args[0], args[1]) # можно прописать res = func(*args)
                t2 = time()
                sum_time += t2 - t1
            return res, t2 - t1, sum_time
        return wrapper
    return deco

@external(1000000) # декоратор с параметром (1000)
def calc(a, b):
    return a + b # можно добавить объекты вычисления

# print(external(1000000)(calc)(5, 2))

print(calc(2, 3))

# t1 = time()
# print(func(2, 3))
# t2 = time()