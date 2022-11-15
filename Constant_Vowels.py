'''
Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output

ee
Ioo
Oeo
eeeee
Explanation

ee is located between consonant d and f.
Ioo is located between consonant k and m.
Oeo is located between consonant p and r.
eeeee is located between consonant t and t.
'''
inp=input()
consonant=0
vowels=0
v=""
v1=[]
for i in range(len(inp)):
	if inp[i] in 'aeiouAEIOU':
		vowels+=1
		v+=inp[i]
	if inp[i] not in 'aeiouAEIOU':
		vowels=0
	if vowels==0 and v!="":
		if len(v)>1:
			v1.append(v)
		v=""
match=""
for i in range(len(v1)):
	n=len(v1[i])
	index=inp.index(v1[i])
	if (inp[index-1] and inp[index+n]) in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
		match+=v1[i]
		match+="\n"
if match=="":
	print(-1)
else:
    print(match)