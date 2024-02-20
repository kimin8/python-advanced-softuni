n = int(input())

def print_upper_rhombus(size):
    for row in range(1, size+1):
        print(" "*(size-row), "* "*row)


def print_lower_rhombus(size):
    for row in range(size-1, 0, -1):
        print(" " * (size - row), "* " * row)


def print_rhombus(width):
    print_upper_rhombus(width)
    print_lower_rhombus(width)


print_rhombus(n)
