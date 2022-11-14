inp=input()
length=int(input())
n=len(inp)
str1=""
sum1=0
for i in range(n):
	if sum1<n:
		str1+=inp[sum1:sum1+length]
		str1+="\n"
		sum1+=length
print(str1)