def dekorator(func):
    def wrapper(*args, **kwargs):
        print(args)
        func(*args, **kwargs)
        return sum(args)
    return wrapper
@dekorator
def f1(a, b):
    print('f1')

print(f1(1, 3))
