def get_list():
    for i in [1, 2, 3, 4]:
        yield i

a = get_list()
for i in a:
    print(i)
