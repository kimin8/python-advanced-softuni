def rectangle(length, width):
    if not (type(length) == int and type(width) == int):
        return "Enter valid values!"
    def area():
        return length * width
        
    def perimeter():
        return 2 * (length + width)
        
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"

print(rectangle('2', 10))