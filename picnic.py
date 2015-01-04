case = 0
totalCase = input()

def countPairs(students, isFriend):
    #   students not exist
    if len(students) == 0:
        return 0
    #   students only two, friend
    if len(students) == 2 and isFriend[students[0]][students[1]]:
        return 1
    #   students only two, not friend
    if len(students) == 2 and not(isFriend[students[0]][students[1]]):
        return 0

    #   counting
    result = 0
    for i in range(1, len(students)):
        if isFriend[students[0]][students[i]]:
            __students = list(students)
            __students.pop(i)
            __students.pop(0)
            result += countPairs(__students, isFriend)
    return result


while totalCase != case:
    input = raw_input().split(" ")
    studentsNum, friendCase = int(input[0]), int(input[1])

    #   initialize isFriend, studentsNum x studentsNum matrix
    isFriend = []
    for i in range(studentsNum):
        row = []
        for j in range(studentsNum):
            row.append(False)
        isFriend.append(row)

    #   setup isFriend matrix
    input = raw_input().split(" ")
    for j in range(0, len(input), 2):
        isFriend[int(input[j])][int(input[j + 1])] = True
        isFriend[int(input[j + 1])][int(input[j])] = True

    #   search for case from data
    print countPairs(range(studentsNum), isFriend)

    case = case + 1
