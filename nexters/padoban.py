total_case = int(input())
case_index = 0

f = [1, 1, 1, 2, 2]

while case_index < total_case:
    n = int(input())
    for i in range(0, n):
        if len(f) == i + 1:
            f.append(f[i] + f[i - 4])
    print(f[n - 1])
    case_index += 1
