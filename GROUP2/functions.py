a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
c = int(input("Enter Last Number"))

def sumAndMulti(a1=5, b1=5, c1=5):  
    # This function ....
    """ This function ... """  
    d = a1 + b1 
    e = d*c1
    print(a1)
    
    return(e)
    

print(sumAndMulti(a1=a, b1 = b))
print(sumAndMulti(b1 = b))
print(sumAndMulti())
print(sumAndMulti.__doc__)