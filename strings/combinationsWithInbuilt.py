# You are given a string . 
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.
# Sample Input:
# HACK 2

from itertools import combinations_with_replacement
def combinations(string,k):
	temp=[]
	comb=combinations_with_replacement(sorted(string),k)
	for x in comb:
		print ("".join(x))
combinations("abc",3) 