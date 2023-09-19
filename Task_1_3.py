x=int(input('введите число X'))
y=int(input('введите число Y'))
a=(x+y)
b=(x-y)
c=(x*y)
d=(x/y)
e=(x//y)
if (a<b and a>c and a>d and a>e):
    print(a)
elif (a>b and a<c and a>d and a>e):
    print(a)
elif (a>b and a>c and a<d and a>e):
    print(a)
elif (a>b and a>c and a>d and a<e):
    print(a)

elif (b<a and b>c and b>d and b>e):
    print(b)
elif (b>a and b<c and b>d and b>e):
    print(b)
elif (b>a and b>c and b<d and b>e):
    print(b)
elif (b>a and b>c and b>d and b<e):
    print(b)

elif (c<=a and c>=b and c>=d and c>=e):
    print(c)
elif (c>=a and c<=b and c>=d and c>=e):
    print(c)
elif (c>=a and c>=b and c<=d and c>=e):
    print(c)
elif (c<=a and c>=b and c>=d and c<=e):
    print(c)

elif (d<=a and d>=b and d>=c and d>=e):
    print(d)
elif (d>=a and d<=b and d>=c and d>=e):
    print(d)
elif (d>=a and d>=b and d<=c and d>=e):
    print(d)
elif (d >= a and d >= b and d >= c and d <= e):
    print(d)
else:
    print(e)