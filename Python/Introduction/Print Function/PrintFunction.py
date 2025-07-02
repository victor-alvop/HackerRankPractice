n = int(input())
my_list = []
for i in range(n):
    my_list.append(str(i+1))

my_list_print = ''.join(my_list)
print(my_list_print)
print(type(my_list_print))


