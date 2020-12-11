src = input()
result = input()

while len(result):
    if len(result) == len(src):
        if result == src:
            print("1")
        else:
            print("0")
    if result[-1] == 'A':
        result = result[:-1]
    elif result[-1] == 'B':
        result = result[:-1]
        result = result[::-1]
