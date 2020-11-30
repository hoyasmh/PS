n=int(input())
l=[int(input()) for i in range(n)]
print([l[-1]*(l[1]//l[0]),l[-1]+(l[1]-l[0])][l[0]-l[1]==l[1]-l[2]])

    
