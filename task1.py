# вариант_4_Польша


WHITE = '\u001b[48;5;255m'
RED = '\u001b[48;5;160m'
END = '\u001b[0m'


def draw_poland(width):
    length = (width // 5) * 8
    # рекомендованные размеры: length = 10k; нужно, чтобы получить соотношение длины к ширине 8/5 и белая и красная полосы состояли из одинакового целого числа строк
    colors = [WHITE, RED]
    for i in range (width):
        print(f"{colors[i//(width // 2)]}{' ' * length}{END}")


if __name__ == "__main__":
    draw_poland(10)
