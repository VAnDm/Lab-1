import sys
sys.stdin = open('sequence.txt', 'r')


from math import ceil
from math import floor


RED = '\u001b[48;5;160m'
BLUE = '\u001b[48;5;21m'
END = '\u001b[0m'
COLORS = [RED, BLUE]



# добавляем в функцию округления число знаков после запятой (по умолчанию 0), так как хотим получить на выходе тип данных int или float, смиримся с тем, что будут отбрасываться нули в конце
def true_round(x, r = 0):
    if (x * (10 ** r)) % 1 < 0.5:
        a = floor(x * (10 ** r))
    else:
        a = ceil(x * (10 ** r))
    if r != 0:
        a = a / (10 ** r)
    return a


# функция рисует горизонтальную столбчатую диаграмму массива чисел, maxlen - длина полосы соответствующей самому большому числу в массиве (по умолчанию 100), числа отображаются в виде десятичной дроби с не более чем 3 знаками после запятой
def draw_chart(numbers, maxlen = 100):
    a = max(numbers)
    longest = 0
    for i in range(len(numbers)):
        y = true_round(numbers[i], 3)
        longest = max(longest, len(f"{y}"))
    for i in range(len(numbers)):
        print(' ')
        length = true_round(maxlen * (numbers[i] / a))
        x = true_round(numbers[i], 3)
        print(f"{' ' * (longest + 1)}{COLORS[i % 2]}{' ' * length}{END}")
        print(f"{' ' * (longest - len(f"{x}"))}{x} {COLORS[i % 2]}{' ' * length}{END}")
        print(f"{' ' * (longest + 1)}{COLORS[i % 2]}{' ' * length}{END}")


modules = []
for i in range(250):
    a = float(input())
    modules.append(abs(a))
firsts = sum(modules[0:125]) / 125
seconds = sum(modules[125:250]) / 125
draw_chart([firsts, seconds])