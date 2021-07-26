def three_args(*a):
    int(a)
    for i in a:
        print("var" + i + "=" + a)


list = [24, 56, 1]
three_args(*list)
print(24)
