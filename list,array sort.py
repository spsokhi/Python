=[23,26,.358,1256.66,55,55.5]
print("Displaying without sort")
for i in range(0,len(a)):
    print(a[i])

print("Sorting ----")
temp=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("array after sorting is ")
for i in range(0,len(a)):
    print(a[i])
