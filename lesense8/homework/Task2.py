# Дана последовательность натуральных чисел, завершающаяся числом 0. Определите,
# какое наибольшее число подряд идущих элементов этой последовательности равны друг другу и что это за элемент.
# Т.е. если программе на вход подать последовательность [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5],
# то на печать программа должна вывести числа 4 и 3, где 4 - повторяющийся элемент, 3 - количество повторений

list = [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5]
dict = {}
a = 0
b = 0
for chis in list:
    if chis == 0:
        max = list[0]
        break
    else:
        dict[chis] = 0
for chis in list:
        if chis == 0:
            break
        else:
            dict[chis] += 1
for i in dict:
    if max < dict[i]:
        max=dict[i]
        a=i
#     new_list = []
# for chis in dict:
#     new_list.append(chis)
# for i in len.list:
print(dict)
print(a,max)
#print(new_list)

