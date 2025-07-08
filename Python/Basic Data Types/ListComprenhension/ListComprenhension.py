x = int(input('Enter x '))
y = int(input('Enter y '))
z = int(input('Enter z '))
n = int(input('Enter n '))

total_permutations = (x+1)*(y+1)*(z+1)
#print(f'Combinaciones: {total_permutations}')

result = [ [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n ]

print(result)