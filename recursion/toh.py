#Tower of Hanoi
def Toh(size,from_stack,to_stck,spare_stck):
	if size==1:
		print "Move disk from",from_stack,"to",to_stck
	else:
		Toh(size-1,from_stack,spare_stck,to_stck)
		Toh(1,from_stack,to_stck,spare_stck) 
		Toh(size-1,spare_stck,to_stck,from_stack)
Toh(3,'From_stk','To_stk','temp_stk')
