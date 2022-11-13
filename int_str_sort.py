inp=input()
lower=[]
upper=[]
odd_digit=[]
even_digit=[]
for i in inp:
	if i in 'abcdefghijklmnopqrstuvwxyz':
		lower.append(i)
	elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		upper.append(i)
	elif (int(i)%2)==0:
		even_digit.append(i)
	elif (int(i)%2)!=0:
		odd_digit.append(i)
lower.sort()
upper.sort()
odd_digit.sort()
even_digit.sort()
sort=lower+upper+odd_digit+even_digit
print(*sort,sep="")