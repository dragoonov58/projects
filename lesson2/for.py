num = int(input('Сколько элементов будет в списке?'))
my_list = []
for i in range(num):
    element = int(input(f'Введите число {i+1}    '))
    my_list.append(element)

print('Созданный список:')
print(my_list)

for i in range(num):
    my_list[i] = my_list[i]+1

print('Список, в котором каждый элемент увеличен на единицу:')
print(my_list)