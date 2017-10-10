# You are given a string . 
# Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
# Sample Input:
# HACK 2

from itertools import permutations

def permutationOFStr(string,k):
	perm=list(permutations(sorted(string),k))
	for x in perm:
		print "".join(x)
permutationOFStr("aba",2)