class ValueCannotBeNegative(Exception):
    """ Raises an error if the given number is negative """
    pass

for _ in range(5):
    num = int(input())

    if num < 0:
        raise ValueCannotBeNegative