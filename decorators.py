# Type-1:
def func1():
    print("*"*50)
    print("result")
    print("*"*50)
func1()

#Type-2:

def pretty(func):
    print("*"*50)
    func()
    print("*"*50)

def fnc():
    print("Hello")

pretty(fnc)

# Type-3 Higher Order Functions:

def pretty(f):
    def inner():
        print("*"*50)
        f()
        print("*"*50)
    return inner

new_func1=pretty(fnc)
new_func1()

@pretty
def fnc():
    print("Hello")
fnc()