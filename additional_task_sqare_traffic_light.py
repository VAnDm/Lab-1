import time
import os


RED = '\u001b[48;5;160m'
YELLOW = '\u001b[48;5;220m'
GREEN = '\u001b[48;5;34m'
GREY = '\u001b[48;5;240m'
BLACK = '\u001b[48;5;16m'
END = '\u001b[0m'


def start_traffic_ligth(n, pause = 3):
    while True:
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {RED}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {GREY}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {GREY}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        time.sleep(pause)

        os.system("cls")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {GREY}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {YELLOW}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {GREY}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        time.sleep(pause)

        os.system("cls")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {GREY}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {GREY}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        for i in range(n):
            print(f"{BLACK} {GREEN}{' ' * (2 * n)}{BLACK} {END}")
        print(f"{BLACK}{' ' * (2 * (n + 1))}{END}")
        time.sleep(pause)

        os.system("cls")


if __name__ == "__main__":
    start_traffic_ligth(3)