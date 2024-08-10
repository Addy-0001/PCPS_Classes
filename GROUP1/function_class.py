x = 1
def func1(a=1, b=2):
    """
    This is a docstring
    """
    # This is a comment
    print(a)
    return a + b
    
op = func1(b=6, a = 5)
op2 = func1()
op3 = func1(10)
print(op3)
print(op)
print(func1.__doc__)
print(op2)
print(a)