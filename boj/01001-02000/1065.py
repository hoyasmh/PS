n=int(input())
if n<100:
    print(n)
else:
    list1=[list(str(i)) for i in range(100,n+1)]
    count=0
    for i in range(len(list1)):
        if int(list1[i][1])*2==int(list1[i][0])+int(list1[i][2]):
            count+=1
    print(count+99)
