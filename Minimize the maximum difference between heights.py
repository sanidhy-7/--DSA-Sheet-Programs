arr=list(map(int,input().split())) 
k=int(input())
arr.sort()
size=len(arr)
ans=arr[-1]-arr[0]
smallest=arr[0]+k 
largest=arr[-1]-k 
for i in range(size-1):
    if(arr[i+1]-k<0):
        continue
    mini=min(smallest,arr[i+1]-k)
    maxx=max(largest,arr[i]+k)
    ans=min(ans,maxx-mini)
print(ans)


