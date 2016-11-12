x = float(input("Enter the number : "))
l = 0.0
u = x
diff = 0.0000000000000000000000001

guess = (l + u) / 2
while abs(guess ** 3 - x) > diff:
    if guess**3 > x:
        u = guess
    elif guess**3 < x:
        l = guess
    guess = (l + u) / 2

print ("Cube root of ",x," is ",guess)
