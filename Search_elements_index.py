'''
Task:
You are given a string S.
Your task is to find the indices of the start and end of string k in S.

Input Format:
The first line contains the string S.
The second line contains the string k.

Sample Input:

aaadaa
aa

Sample Output:

(0, 1)  
(1, 2)
(4, 5)
'''
inp=input()
key=input()
start=0
end=len(key)
value=""
n=len(inp)
index=[]
for j in range(len(inp)):
	for i in range(start,end):
		try:
			value+=inp[i]
		except:
			break
	temp=[]
	if value==key:
		temp.append(start)
		temp.append(end-1)
	if len(temp)!=0:
		index.append(tuple(temp))
	start+=1
	end=start+len(key)
	value=""
if len(index)!=0:
	print(*index,sep="\n")
else:
	print((-1,-1))