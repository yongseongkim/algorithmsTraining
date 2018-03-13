# -*- coding:utf8 -*-
import fnmatch


total_case = input()
case_index = 0

#
#	fnmatch를 이용한 야매 방법...
#

while case_index < total_case:
    wildcard = raw_input()
    target_number = input()
    targets = []
    for i in xrange(target_number):
    	targets.append(raw_input())
    results = []
    for i in xrange(len(targets)):
    	if fnmatch.fnmatch(targets[i], wildcard):
    		results.append(targets[i])
    results.sort()
    for i in xrange(len(results)):
    	print results[i]
    case_index += 1