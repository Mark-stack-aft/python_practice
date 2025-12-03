def func():
    x = 20
    print(x)

func()

def func1():
    global x
    x = 10
    print(x)

func1()

print(x)