t=int(raw_input())
for _ in range(t):
	no_of_coins=int(raw_input())
	coinsArr=list(map(int,raw_input().split()))
	charlie=True
	for i in range(0,no_of_coins):
		while coinsArr[i]>1:
			if coinsArr[i]%2==0:
				coinsArr[i]-=coinsArr[i]/2
				if charlie:
					charlie=False
				elif not charlie:
					charlie=True
	if charlie:
		print "Alan"
	else:
		print "charlie"
