a = int(input('Insert a value: '))


if 1 <= a and a <= 20:
    [print(i ** 2) for i in range(a)]
else:
    print ('error')