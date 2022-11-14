inp=input()
key=int(input())
substring=[]
for i in range(len(inp)):
	s=inp[i:key+i]
	if len(s)==key:
		substring.append(s)
vowels=""
vowels_len=0
length=[]
for i in range(len(substring)):
	vowels_len=0
	vowels+=substring[i]
	for j in range(len(vowels)):
		if vowels[j] in 'aeiouAEIOU':
			vowels_len+=1
	length.append(vowels_len)
	vowels=""
index=max(length)
if index==0:
	print("Not found!")
else:
	print(substring[length.index(index)])
'''
string_is = input()
sub = int(input())
length = len(string_is)
sub_ar = [string_is[i:j+1] for i in range(length) for j in range(i,length)]
sub_ar_is = []
for each in sub_ar:
  if len(each) == 5:
    sub_ar_is.append(each)
data_dict = {}
data = ['a','e','i','o','u']
for each in sub_ar_is:
  count = 0
  for each_is in data:
    count = count + each.count(each_is)
  data_dict.update({each:count})
print(max(data_dict, key=data_dict.get))
'''