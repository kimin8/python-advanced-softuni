def operate(operator, *args):
    total = 0

    def sum_numbers(x, y):
        return x + y
    def subtract_numbers(x, y):
        return x - y
    def multiply_numbers(x, y):
        return x * y
    def divide_numbers(x, y):
        return x / y
    
    if operator == "+":
        for el in args:
            total = sum_numbers(total, el)
        return total
    elif operator == "-":
        total = args[0]
        for i in range(1, len(args)):
            total = subtract_numbers(total, args[i])
        return total
    elif operator == "*":
        total = 1
        for el in args:
            total = multiply_numbers(total, el)
        return total
    elif operator == "/":
        total = args[0]
        for i in range(1, len(args)):
            total = divide_numbers(total, args[i])
        return total
    
print(operate("-", 5, 3, 4, 3, 2))