inp=input().lower()
vowels=['a','e','i','o','u']
consonant=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
input_strings=[*inp]
def vowel(input_string):
	temp=[]	
	input_str=""
	for i in range(len(input_string)):
		length1=0
		length2=0
		n=len(input_string)
		sum1=i+1
		while n>1:
			if input_string[length1] in vowels:
				for i in range(length1,length2+sum1):
					input_str+=input_string[i]
				if len(input_str)==sum1:
					temp.append(input_str)
				input_str=""
			length1+=1
			length2+=1
			break
			n-=1
		if length1==0:
			length5=length1
		else:
			length5=length1+1
		n=len(input_string)
		while n>1:
			try:
				if input_string[length5-1] in vowels:
					if length5==0:
						length3=length5
						length4=length5+sum1
					else:
						length3=length5-1
						length4=(length5-1)+sum1
					for i in range(length3,length4):
						try:
							input_str+=input_string[i]
						except:
							break
					if input_str not in temp:
						if len(input_str)==sum1:
							temp.append(input_str)
					input_str=""
			except:
				break
			n-=1
			length5+=1
	return temp
def consonants(input_string):
	temp=[]	
	input_str=""
	for i in range(len(input_string)):
		length1=0
		length2=0
		n=len(input_string)
		sum1=i+1
		while n>1:
			if input_string[length1] in consonant:
				for i in range(length1,length2+sum1):
					input_str+=input_string[i]
				if len(input_str)==sum1:
					temp.append(input_str)
				input_str=""
			length1+=1
			length2+=1
			break
			n-=1
		if length1==0:
			length5=length1
		else:
			length5=length1+1
		n=len(input_string)
		while n>1:
			try:
				if input_string[length5-1] in consonant:
					if length5==0:
						length3=length5
						length4=length5+sum1
					else:
						length3=length5-1
						length4=(length5-1)+sum1
					for i in range(length3,length4):
						try:
							input_str+=input_string[i]
						except:
							break
					if input_str not in temp:
						if len(input_str)==sum1:
							temp.append(input_str)
					input_str=""
			except:
				break
			n-=1
			length5+=1
	return temp
vowels=[*vowel(input_strings)]
consonant=[*consonants(input_strings)]
check=[]
for i in range(len(input_strings)):
	n=len(input_strings)
	sum1=i+1
	length1=0
	length2=sum1
	while n>=sum1:
		str2=""
		for i in range(length1,length2):
			try:
				str2+=input_strings[i]
			except:
				break
		check.append(str2)
		n-=1
		length1+=1
		length2=length1+sum1
stuart=0
kevin=0
for i in range(len(consonant)):
	for j in range(len(check)):
		if consonant[i]==check[j]:
			stuart+=1
for i in range(len(vowels)):
	for j in range(len(check)):
		if vowels[i]==check[j]:
			kevin+=1
if stuart>kevin:
	print("Stuart ",stuart)
elif stuart<kevin:
	print("Kevin ",kevin)
elif stuart==kevin:
	print("Draw")