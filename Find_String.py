inp=input()
find=input()
n=len(find)
f=[]
for i in range(len(inp)):
	temp=inp[i:n]
	if len(temp)==len(find):
		f.append(temp)
	n+=1
sum1=0
for i in range(len(f)):
	if find==f[i]:
		sum1+=1
print(sum1)