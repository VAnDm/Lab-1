# вариант 4 функция x^0.5


from math import sqrt
from math import floor
from math import ceil


# используем свое округление, так как встроенное - банковское
def true_round(x):
    if x % 1 < 0.5:
        return floor(x)
    else:
        return ceil(x)


def draw_sqrt(height):
    # height - количество строк в изображаемом графике; считаем что если одна строка соответствует 1, то столбец соответствует 1/2, так как символ вдвое уже строки
    length = 2 * (height ** 2)
    table = []

    # рисуем координатные оси
    for i in range(height + 1):
        table.append([' '] * (length + 2))
    table[0][0] = 'y'
    table[0][1] = '^'
    for i in range(1, height + 1):
        table[i][1] = '|'
    table.append(['-'] * (length + 2))
    table[height + 1][1] = '+'
    table[height + 1][length + 1] = '>'
    table.append([' '] * (length + 2))
    table[height + 2][0] = '0'
    table[height + 2][1] = '|'
    table[height + 2][length + 1] = 'x'
    
    # рисуем график
    yprev = 0
    for i in range(length):
        y = true_round(sqrt(i / 2))
        table[height - y][i + 2] = '_'
        if y > yprev:
            table[height - y + 1][i + 1] = '/'
        yprev = y
    
    # выводим график
    for i in range(height + 3):
        print(''.join(table[i]))
        #print(*table[i], sep = '')

if __name__ == "__main__":
    draw_sqrt(9)



