from collections import defaultdict
row=int(input())
col=int(input())
inp=[]
for i in range(row):
    inp.append(list(map(int,input().split())))
def getCount(rows, columns, sides):
    ans = 0
    umap = defaultdict(int)
    for i in range(rows):
        ratio = sides[i][0] / sides[i][1]
        umap[ratio] += 1
    for x in umap:
        value = umap[x]
        if (value > 1):
            ans += (value * (value - 1)) / 2
    return ans
print(int(getCount(row, column, inp)))