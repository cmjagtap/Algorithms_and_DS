#Array is given votes as a voter_no find who will win election
def winnerElection(array):
	if not array:
		return None
	else:
		votecount=maxVote=0
		winner=array[0]
		for x in xrange(0,len(array)):
			votecount=0
			for y in xrange(1,len(array)):
				if array[x]==array[y]:
					votecount+=1
			if maxVote<votecount:
				maxVote=votecount
				winner=array[x]
		return winner,maxVote

votes=[1,2,3,2,1,2,2,3,2,2]
x,y=winnerElection(votes)
print "winner is",x,"with votes",y
