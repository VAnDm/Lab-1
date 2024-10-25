WHITE = '\u001b[48;5;255m'
RED = '\u001b[48;5;160m'
END = '\u001b[0m'

def draw_poland():
    length = 32
    width = 10
    # reccomended size: length = 16x; width = 5x; x%2 == 0
    colors = [WHITE, RED]
    for i in range (width):
        print(f"{colors[i//(width // 2)]}{' ' * length}{END}")
if __name__ == "__main__":
    draw_poland()
