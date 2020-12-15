# https://leetcode.com/problems/task-scheduler/
import collections


def task_scheduler(tasks, n):
    counter = collections.Counter(tasks)
    result = 0
    while True:
        sub_count = 0

        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0 이하인 아이템을 목록에서 제거
            counter += collections.Counter()

        if not counter:
            break
        result += n - sub_count + 1
    return result

print(task_scheduler(["A","A","A","B","B","B"], 2)) # 8
print(task_scheduler(["A","A","A","B","B","B"], 0)) # 6
print(task_scheduler(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)) # 16
print(task_scheduler(["A","A","A","B","B","B","C","C","C","D","D","E"], 2)) # 12
