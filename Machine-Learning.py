inputArray = [3, 6, -2, -5, 7, 3]
n=len(inputArray)
s=[]
for i in range(0,n-1):
    if(i==n-1):
        break
    s.append(inputArray[i]*inputArray[i+1])
print(max(s))
print(s)

