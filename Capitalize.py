a=input()
sum1=0
b=[]
for i in range(len(a)):
	if sum1==0:
		b.append(a[i].upper())
	else:
		b.append(a[i])
	sum1+=1
	if a[i]==" ":
		sum1=0
a=""
for i in range(len(b)):
	a+=b[i]
print(a)