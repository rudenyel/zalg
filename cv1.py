#def gcd(x, y):
#    while(x!=y):
#        if x > y:
#            x = x - y
#        else:
#            y = y -x
#    print(x)

#gcd(30,12)

def maxvalue(a):
    m = a[0]
    idx = 0
    for i in range(1, len(a)):
        if a[i] > m:
            m = a[i]
            idx = i
    return (idx, m)


a = [1, 6, 9, 34, 78, 90, 50]
print(maxvalue(a))

