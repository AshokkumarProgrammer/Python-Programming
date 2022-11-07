#Here less than 25 number will be correctly shown
inp=int(input())
decbin=[]
decoct=[]
dechex=[]
for i in range(inp):
	s=""
	sum1=i+1
	binary=[]
	while (sum1>=1):
		t1=sum1//2
		binary.append(sum1%2)
		sum1=t1
	binary.reverse()
	l1=list(map(str,binary))
	decbin.append(''.join(l1))
	binary=[]
for j in range(inp):
	sum2=j+1
	octal=[]
	while (sum2>=1):
		t2=sum2//8
		octal.append(sum2%8)
		sum2=t2
	octal.reverse()
	l2=list(map(str,octal))
	decoct.append(''.join(l2))
	octal=[]
temp=65
for k in range(inp):
	sum3=k+1
	hexa=[]
	while (sum3>=1):
		t3=sum3//16
		s=sum3%16
		iv=k+1
		if iv>=10 and iv<=15:
			hexa.append(chr(int(temp)))
			temp+=1
		else:
			hexa.append(s)
		sum3=t3
	hexa.reverse()
	l3=list(map(str,hexa))
	dechex.append(''.join(l3))
	hexa=[]
for i in range(inp):
	print(i+1," ",decoct[i]," ",dechex[i]," ",decbin[i])