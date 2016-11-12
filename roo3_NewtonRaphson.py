x = float(input("Enter your Number : "))
y = 4
h = lambda x,y: ((x**3) - y) / (3 * x**2)
y1 = 0.0
d = 0.000000000000000000000000001
count = 0
while abs(y - y1) > d:
    y1 = y
    y = y - h(y,x)
    count += 1
print ("cube root of ", x, "is ",y)
