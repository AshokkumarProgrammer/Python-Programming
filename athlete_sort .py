nm = input().split()
n = int(nm[0])
m = int(nm[1])
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input())
arr=sorted(arr, key=lambda arr:arr[k])
for x in arr: 
    for i in x:  
        print(i, end = " ")
    print()