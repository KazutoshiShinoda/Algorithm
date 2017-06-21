# -*- coding: utf-8 -*-

#########################
#~What is this function for?~
#
#There are N balls labeled with the first N uppercase letters. The balls have pairwise distinct weights.
#You are allowed to ask at most Q queries. In each query, you can compare the weights of two balls (see Input/Output section for details).
#Sort the balls in the ascending order of their weights.
#
#This task is the Problem B of the practice contest of "AtCoder"(http://practice.contest.atcoder.jp/tasks/practice_2).
#########################
import sys
[N, Q] = list(map(int, input().split()))
Data = [chr(i) for i in range(65, 65+N)]
data = []

def Binary(data, start, end, c):
	p = int((start + end)/2)
	print("? "+data[p]+" "+c)
	sys.stdout.flush()
	ans = input()
	light = data[start:p]
	heavy = data[p+1:end+1]
	l_length = len(light)
	h_length = len(heavy)
	if ans=='<':
		if h_length == 0:
			pos = p
		else:
			pos = Binary(data, p+1, end, c)
	else:
		if l_length == 0:
			pos = p-1
		else:
			pos = Binary(data, start, p-1, c)
	return pos
	
if N != 5:
	data.append(Data[0])
	for i in range(1, N):
		c = Data[i]
		pos = Binary(data, 0, i, c)
		light = data[:pos+1]
		heavy = data[pos+1:]
		light.append(c)
		light.extend(heavy)
		data = light
else:
	print("? "+Data[0]+" "+Data[1])
	sys.stdout.flush()
	H1 = input()
	print("? "+Data[2]+" "+Data[3])
	sys.stdout.flush()
	H2 = input()
	
print("! "+"".join(data))