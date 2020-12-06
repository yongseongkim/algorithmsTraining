# 2020년 카카오 신입 블라인드 채용 1차 코딩 테스트
# https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/
# caution: 10a100b1000c

import sys
import collections

total_case = int(input())
case_index = 0


def solve(s):
    lens = len(s)
    mnlen = lens
    for window in range(int(lens / 2), 0, -1):
        chunks = [s[i:i+window] for i in range(0, lens, window)]
        compressed = []
        count = 0
        for chunk in chunks:
            if len(compressed) == 0:
                compressed.append(chunk)
                count = 1
            else:
                if compressed[-1] == chunk:
                    count += 1
                else:
                    if count > 1:
                        compressed.insert(0, str(count))
                    compressed.append(chunk)
                    count = 1
        if count > 1:
            compressed.insert(0, str(count))
        mnlen = min(mnlen, len(''.join(compressed)))
    return mnlen
                
while case_index < total_case:
    # do something
    print(solve(input()))
    case_index += 1
