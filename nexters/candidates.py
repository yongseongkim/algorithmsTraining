# -*- coding:utf-8 -*-

limit = int(input())
_ = int(input())
votes = [int(num) for num in input().split(' ')]

sum_votes = dict()
candidates = []
for vote in votes:
    if sum_votes.get(vote) is None:
        sum_votes[vote] = 1
    else:
        sum_votes[vote] = sum_votes[vote] + 1
    if vote in candidates:
        candidates.remove(vote)
    if len(candidates) == limit:
        # 마지막 요소는 가장 오래되고 vote가 적다. 삭제하고 새로 추가할 요소의 위치를 정한다.
        sum_votes[candidates[-1]] = 0
        del candidates[-1]
        for i in range(0, len(candidates)):
            if sum_votes[vote] >= sum_votes[candidates[i]]:
                candidates.insert(i, vote)
                break
    else:
        # 지금 vote 한 요소를 앞으로 앞으로 이동시킨다.
        for i in range(0, len(candidates)):
            if sum_votes[vote] >= sum_votes[candidates[i]]:
                candidates.insert(i, vote)
                break
    if not vote in candidates:
        candidates.append(vote)
for candidate in sorted(candidates):
    print(candidate, end=' ')
