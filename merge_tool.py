s=input()
k=int(input())
ln=len(s)
for i in range(0,ln,k):
    ss=s[i:i+k]
    sss=[]
    for x in ss:
        if x not in sss:
            sss.append(x)

    print (''.join(sss))