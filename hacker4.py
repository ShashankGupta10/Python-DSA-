e = int(input(""))
f = int(input(""))
g = int(input(""))
h = int(input(""))

def check(a, b, c, d):
    if a ==c and b == d:
        return True
    
    elif a > c or b > d:
        return False
    
    elif a == c:
        check(a, a + b, c, d)

    elif b == d:
        check(a + b, b, c, d)
    
    elif c < d:
        check(a + b, b, c, d)

    elif d < c:
        check(a, a + b, c, d)
        
    else: 
         return False

if check(e, f, g, h) == True:
    print("possible")

else: 
    print("no possible")
