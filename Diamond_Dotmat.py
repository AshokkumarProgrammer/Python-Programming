inp=list(map(int, input().split(" ")))
input1=[]
for i in range(len(inp)-1):
	input1.append(inp)
a=input1[0][0]
b=input1[0][1]
a1=int(a/2)
sum1=1
sum2=3
l=[]
for i in range(a1):
	temp=int((b-(sum1*sum2))/2)
	l.append('-'*temp)
	l.append('.|.'*sum1)
	l.append('-'*temp)
	if(i!=a1-1):
		l.append('\n')
	sum1+=2
print(*l,sep="")
t=int((b-7)/2)
print('-'*t,"WELCOME",'-'*t,sep="")
t2=len(l)
l1=[]
while t2>0:
	l1.append(l[t2-1])
	t2-=1
print(*l1,sep="")