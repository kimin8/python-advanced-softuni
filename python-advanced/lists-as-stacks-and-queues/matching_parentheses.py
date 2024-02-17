exp = input()
stack = []

for i in range(0, len(exp)):
    if exp[i] == "(":
        stack.append(i)
    elif exp[i] == ")":
        print(exp[stack.pop():i+1])