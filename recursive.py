def F(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return F(n-1) + F(n-2) + F(n-3) 

n = int(input("please enter a number: "))
print("F(%d)"  %n + " = " + '%d' %F(n))
