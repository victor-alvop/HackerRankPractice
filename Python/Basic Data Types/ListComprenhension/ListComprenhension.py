x = int(input('Enter x '))
y = int(input('Enter y '))
z = int(input('Enter z '))

total_permutations = x*y*z
permutations_list = []
[permutations_list.append([i]) for i in range(total_permutations)]

#matrix = [[[i for i in range(y)] for _ in range(x)] for _ in range(z)]
#matriz_3d = [[[0 for _ in range(columnas)] for _ in range(filas)] for _ in range(profundidad)]

print(permutations_list)