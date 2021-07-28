# Nomber 1
my_dict1 = {"Hello": "Привет", "Where": "Где", "Cat": "Кот"}

# def Angl(rus):
#     angl=my_dict1[rus]
#     return angl
#
#
# def
# rus = input()
# angl = input()
#
# Angl(rus)

my_dict2 = {
    value: key
        for key, value in my_dict1.items()
}

print(my_dict2)
