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

[N, Q] = map(int, raw_input().split())
Data = [chr(i) for i in range(65, 65+N)]
cal_time = 0
def QuickSort(data, start, end):
	global cal_time
	n = end - start + 1
	pivot = int(n/2.0)
	P = data[pivot]
	light = []
	heavy = []
	for i in range(start, pivot):
		cal_time += 1
		print "? "+data[i] + " " + data[pivot]
		ans = raw_input()
		if ans == '>':
			heavy.append(data[i])
		else:
			light.append(data[i])
	for i in range(pivot+1, end+1):
		cal_time += 1
		print "? "+data[pivot] + " " + data[i]
		ans = raw_input()
		if ans == '<':
			heavy.append(data[i])
		else:
			light.append(data[i])
	l_length = len(light)
	h_length = len(heavy)
	
	data[start:start+l_length] = light
	data[start+l_length] = P
	data[start+l_length+1:end+1] = heavy
	
	if l_length >= 2:
		data = QuickSort(data, start, start+l_length-1)
	if h_length >= 2:
		data = QuickSort(data, start+l_length+1, end)
	return data
	
print QuickSort(Data, 0, N-1)
if cal_time < Q:
	print "You complete the sorting task! You are GENIUS!!"