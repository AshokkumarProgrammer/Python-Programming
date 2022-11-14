inp=input()
str1=inp[0]
sum1=0
for i in range(1,len(inp)):
	if inp[i] not in '[@_!#$%^&*()<>?/\\|}{~:].':
		if inp[i]==str1:
			sum1+=1
			print(inp[i])
			break
		str1=""
		str1+=inp[i]
if sum1==0:
	print(-1)