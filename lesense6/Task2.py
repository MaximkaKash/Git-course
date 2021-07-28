def func(i):
    part = 0
    if i % 2 == 0:
        part = i / 2
    else:
        part = i / 2 + 0.5
    return part


my_list = [14, 12, 7]
part_sum = 0
for i in my_list:
    part_sum += func(i)
print(part_sum)
