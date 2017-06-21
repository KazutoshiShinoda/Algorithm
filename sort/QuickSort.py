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
def QuickSort(data, start, end):
	n = end - start + 1
	pivot = int((end+start)/2.0)
	P = data[pivot]
	light = []
	heavy = []
	
	for i in range(start, pivot):
		print("? "+data[i] + " " + data[pivot], flush = True)
		sys.stdout.flush()
		ans = input()
		if ans == '>':
			heavy.append(data[i])
		else:
			light.append(data[i])
			
	for i in range(pivot+1, end+1):
		print("? "+data[pivot] + " " + data[i], flush = True)
		sys.stdout.flush()
		ans = input()
		if ans == '<':
			heavy.append(data[i])
		else:
			light.append(data[i])
	l_length = len(light)
	h_length = len(heavy)
	
	data[start:start+l_length] = light
	data[start+l_length] = P
	data[start+l_length+1:start+l_length+h_length+1] = heavy
	
	if l_length >= 2:
		data = QuickSort(data, start, start+l_length-1)
	if h_length >= 2:
		data = QuickSort(data, start+l_length+1, end)
	return data
	
print("! " + "".join(QuickSort(Data, 0, N-1)))