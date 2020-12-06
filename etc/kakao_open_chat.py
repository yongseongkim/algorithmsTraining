# 2019년 카카오 신입 공채 1차 코딩테스트
# https://tech.kakao.com/2018/09/21/kakao-blind-recruitment-for2019-round-1/#1-%EC%98%A4%ED%94%88%EC%B1%84%ED%8C%85%EB%B0%A9

import sys
import collections

total_case = int(input())
case_index = 0


def open_chat(records):
    result = []
    uid_name = collections.defaultdict(str)
    for record in records:
        record = record.split(' ')
        command = record[0]
        uid = record[1]
        if command == 'Enter' or command == 'Change':
            uid_name[uid] = record[2]
    
    for record in records:
        record = record.split(' ')
        command, uid = record[0], record[1]
        if command == 'Enter':
            result.append("{}님이 들어왔습니다.".format(uid_name[uid]))
        elif command == 'Leave':
            result.append("{}님이 나갔습니다.".format(uid_name[uid]))
    return result

while case_index < total_case:
    # do something
    # records = input().split(',')
    records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(open_chat(records))
    case_index += 1
