def reverse_text(string: str):
    for i in range(len(string)-1, -1, -1):
        yield string[i]

