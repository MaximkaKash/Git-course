# nomber1
from datetime import datetime

car_list = [
    {"sn": 123, "color": "red", "year": 1999},
    {"sn": 153, "color": "yellow", "year": 2005},
    {"sn": 993, "color": "blur", "year": 2021},
    {"sn": 333, "color": "reeee", "year": 2013},
    {"sn": 18, "color": "ya", "year": 1943},
    {"sn": 1833, "color": "f", "year": 1001},
]


def my_decorator(func1):
    def timer(year):
        start_time = datetime.now()
        result = func1(year)
        end_time = datetime.now()
        print(end_time - start_time)
        return result

    return timer


@my_decorator
def func(year):
    new_list = []
    for car in car_list:
        if car["year"] > year:
            new_list.append(car)

    return new_list


def main():
    print(func(2000))


if __name__ == "__main__":
    main()
