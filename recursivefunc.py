#factorial
'''def f(n):
    if n==0:
        return 1
    return n*f(n-1)
a=f(5)
print(a)'''

#fibonacci
'''def f(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return f(n-1)+f(n-2)
a=f(5)
print(a)'''

#powerof2numbers
def p(n,m):
    if m==0:
        return 1
    return n*p(n,m-1)
a=p(2,3)
print(a)
    
