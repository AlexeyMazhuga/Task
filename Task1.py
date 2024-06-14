from time import time

def deco(func):
    def wrapper(*args):
        t1 = time()
        res = func(args[0], args[1]) # можно прописать res = func(*args)
        t2 = time()
        return res, t2 - t1
    return wrapper

@deco # синтаксический сахар, задекорировали функцию, она дополняет исходную функцию для вычисления времени
def calc(a, b):
    return a + b # можно добавить объекты вычисления

print(calc(2, 3))

# t1 = time()
# print(func(2, 3))
# t2 = time()
# print(t2 - t1)
