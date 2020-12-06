import sys

def segment(x, space):
		if x >= len(space):
        return min(space)
    mx_minima = -sys.maxsize
    for i in range(0, len(space) - x, 1):
        if space[i] < mx_minima:
            continue
        minima = min(space[i:i+x])
        mx_minima = max(mx_minima, minima)
    return mx_minima

x = 1
space = [1, 2, 3, 1, 2]
x = 2
space = [1, 1, 1]
# x = 3
# space = [2, 5, 4, 6, 8]
# x = 1
# space = [1000000]
# x = 5
# space = [1, 2, 3, 1, 2]

print(segment(x, space))