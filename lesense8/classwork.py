# nomber1
car_lst = [
    {"sn": 123,"color": "red","year": 1999},
    {"sn":153,"color":"yellow","year": 2005},
    {"sn":993,"color":"blur","year": 2021},
]

def func(year):
new_list=[]
    for car in car_list:
        if car["year"]>year:
           new_list.append(car)
return mew_list

def main():
    print(filter(lambda x:x["year"]>2000,car_list))


if __name__=="__main__":
    main()