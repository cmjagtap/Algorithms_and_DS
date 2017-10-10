# Output Format:Print the sum of the elements of set  on a single line.
# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop 
# discard 6
# remove 5
# pop 
# discard 5

# Sample Output
# 4

n = input()
s = set(map(int, raw_input().split())) 
opr=int(input())
for _ in range(opr):
    temp=raw_input().split()
    if temp[0]=="pop":
        s.pop()
    elif temp[0]=="remove":
        s.remove(int(temp[1]))
    elif temp[0]=="discard":
        s.discard(int(temp[1]))
print sum(s)