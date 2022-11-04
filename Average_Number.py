a=list(map(int, input().split(" ")))
sum=0
if len(a)==1:
    print(format(a[0],".2f"))
else:
	for i in range(len(a)):
	    sum+=a[i]
	avg=(sum/len(a))
	print(format(avg,".2f"))