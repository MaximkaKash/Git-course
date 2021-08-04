# Спортсмен поставил перед собой задачу пробежать в общей сложности Х километров.
# В первый день спортсмен пробежал Y километров, а затем он каждый день увеличивал пробег на 10% от предыдущего.
# Определите номер дня в который спортсмен достигнет своей цели.
# Оформите решение в виде программы, которая на вход принимает числа X и Y и выводит номер найденного дня.


def Run(result, step):
    day = 0
    while result>0:
        result -= step
        step *= 1.1
        day += 1
    return day


def main():
    result = float(input())
    step = float(input())
    day = Run(result, step)
    print(day)


if __name__ == '__main__':
    main()
