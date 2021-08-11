class MyTime:

    """ Класс для слов, определяющий сравнение по длине слов. """

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __gt__(self, other):
        return len(self.word) > len(other)

    def __lt__(self, other):
        return len(self.word) < len(other)

    def __ge__(self, other):
        return len(self.word) >= len(other)

    def __le__(self, other):
        return len(self.word) <= len(other)


def print_hi(name):

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
