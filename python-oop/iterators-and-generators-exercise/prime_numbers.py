from math import sqrt


def get_primes(integers: list):
    for num in integers:
        if num <= 1:
            continue

        for divisor in range(2, int(sqrt(num)) + 1):
            if num % divisor == 0:
                break
        else:
            yield num
