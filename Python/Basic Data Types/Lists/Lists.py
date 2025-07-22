print('hello vekerito')

N = int(input())
my_list = []

for _ in range(N):
    command = input().split()
    command_method = command[0]
    command_values = command[1:]

    if command_method == 'print':
        print(my_list)
    else:
        eval(f"my_list.{command_method}({', '.join(command_values)})")