alphabet='abcdefghijklmnopqrstuvwxyz'
a=[*alphabet]
n=int(input())
temp=[]
t=n
while t>1:
	temp.append(a[t-1])
	t-=1
for i in range(n):
	temp.append(a[i])
length1=len(temp)+(len(temp)-1)
lenght2=length1//2
length3=len(temp)//2
temp2=[]
temp1=[]
for i in range(length3):
	temp2.append(temp[i])
sum1=len(temp)
while sum1>0:
	temp1.append(temp[sum1-1])
	sum1-=1
	if(sum1==length3):
		break
temp4=[]
cal=[]
final=[]
sum2=1
sum3=0
l1=[]
n=len(temp1)
final.append("@")
final.append(temp1[0])
final.append("@")
while (n-1)>0:
	if (n-1)>1:
		final.append("@")
	for i in range(sum2+1):
		final.append(temp1[i])
		final.append("-")
	sum2+=1
	cal=[]
	n-=1
	for i in range(sum3+1):
		temp4.append(temp2[i])
	sum3+=1
	l1=temp4[::-1]
	for i in range(len(l1)):
		final.append(l1[i])
		final.append("-")
	final.pop()
	if (n-1)>0:
		final.append("@")
	temp4=[]
	l1=[]
tn1=[]
n1=len(final)
while n1>0:
	if final[n1-2]==temp1[0]:
		break
	elif final[n1-1]!="-":
		tn1.append(final[n1-1])
	n1-=1
mv=(len(tn1)//2)*2
sy=0
final2=[]
for i in range(len(final)):
	if final[i]=="@":
		final2.append("-"*mv)
		sy+=1
		if sy==2:
			final2.append("\n")
			sy=0
			mv-=2
	else:
		final2.append(final[i])
t2=len(final2)-(len(temp)+(len(temp)-1))
while t2>0:
	final2.append(final2[t2-1])
	t2-=1
print(*final2,sep="")