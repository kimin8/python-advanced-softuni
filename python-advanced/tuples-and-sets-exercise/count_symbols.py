text = input()
symbols = {}

for index in range(len(text)):
    if text[index] in symbols.keys():
        symbols[text[index]] += 1
    else:
        symbols[text[index]] = 1

sorted_keys = sorted(symbols.keys())

for key in sorted_keys:
    print(f"{key}: {symbols[key]} time/s")
