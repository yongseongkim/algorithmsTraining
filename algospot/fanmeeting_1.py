total_case = int(input())
case_index = 0

# 무식하게 세기

def match(hyper_senior, fans):
	for idx in range(len(hyper_senior)):
		if hyper_senior[idx] == 'M' and fans[idx] == 'M':
			return 0
	return 1


def hug(hyper_senior, fans):
	count = 0
	for idx in range(0, len(fans) - len(hyper_senior) + 1):
		count += match(hyper_senior, fans[idx:len(fans)])
	return count

while case_index < total_case:
	hyper_senior = list(input())
	fans = list(input())
	print(hug(hyper_senior, fans))
	case_index += 1
