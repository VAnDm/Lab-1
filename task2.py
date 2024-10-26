# вариант 4 узор d
# примечание: возможно продолжение узора отличается от задуманного, но, так как Вы писали продлить его так, чтобы было похоже на ковер, решил его зациклить)


BLACK = '\u001b[48;5;16m'
WHITE = '\u001b[48;5;255m'
END = '\u001b[0m'


def draw_carpet(table_width):
    # рекомендованные размеры: table_width = 4k + 1; так как узор имеет период 4 по строкам и должен начинаться и заканчиваться сплошной строкой
    table_length = 2 * table_width
    carpet_table = []

    # создание пустой таблицы для генерации закрашенных мест
    for i in range(table_width):
        carpet_table.append([' '] * table_length)
    
    # генерация закрашенных мест
    row_len = table_length
    offset = 0
    for i in range(table_width):
        for j in range(table_length):

            # генерация сплошных линий
            if i % 2 == 0:
                if j >= (table_length - row_len) // 2  and j < table_length - ((table_length - row_len) // 2):
                    carpet_table[i][j] = '#'

            # генерация клеток в пустых линиях с одной закрашенной клеткой
            if (i % 4 == 1 and i < table_width // 2) or (i % 4 == 3 and i > table_width // 2):
                if j == table_length // 2 - 1 or j == table_length // 2:
                    carpet_table[i][j] = '#'
        
            # генерация клеток в пустых линиях с двумя закрашенными клетками    
            if (i % 4 == 3 and i < table_width // 2) or (i % 4 == 1 and i > table_width // 2):
                start = j - offset
                if row_len % 3 == 1:
                    if start == row_len // 3 - 1 or start == row_len // 3 or start == 2 * row_len // 3 or start == 2 * row_len // 3 + 1:
                        carpet_table[i][j] = '#'
                if row_len % 3 == 2:
                    if start == (row_len // 3) or start == (row_len // 3) + 1 or start == 2 * (row_len // 3) or start == 2 * (row_len // 3) + 1:
                        carpet_table[i][j] = '#'
                if row_len % 3 == 0:
                    if start == (row_len // 3) - 2 or start == (row_len // 3) - 1 or start == 2 * (row_len // 3) or start == 2 * (row_len // 3) + 1:
                        carpet_table[i][j] = '#'
        
        # рассчет сдвига начала закрашенной строки
        if i < table_width // 2:
            row_len = row_len - 4
            offset = offset + 2
        else:
            row_len = row_len + 4
            offset = offset - 2

    # отражение узора относительно главной диагонали для заполнения закрашенных столбцов (учитываем растяжение по горизонтали вдвое)
    for i in range(table_width):
        for j in range(table_length):
            if j % 2 == 0 and carpet_table[i][j] == '#':
                carpet_table[j // 2][2 * i] = '#'
                carpet_table[j // 2][2 * i + 1] = '#'

    # вывод цветного узора
    for i in range(table_width):
        s = ''
        fl = 0
        for j in carpet_table[i]:
            if j == '#' and fl == 0:
                fl = 1
                s = f"{s}{BLACK} "
            elif j == ' ' and fl == 1:
                fl = 0
                s = f"{s}{WHITE} "
            else:
                s = f"{s} "
        s = f"{s}{END}"
        print(s)


if __name__ == "__main__":
    draw_carpet(21)
