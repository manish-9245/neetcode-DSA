arr=[1,4,7,2,4,9,0]
for i in range (1,len(arr)):
    j=i-1
    while (j>=0 and arr[j+1]<arr[j]):
        tmp=arr[j+1]
        arr[j+1]=arr[j]
        arr[j]=tmp
        j=j-1
print(arr)
#4.3.2.1
n=4