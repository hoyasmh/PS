y=[0,1,-1,0,0,1,1,2,3,3,4,4,5]
w=["Wednes","Thurs","Fri","Satur","Sun","Mon","Tues"]
a,b=map(int,input().split())
print(w[(30*(b-1)+y[b-1]+a)%7]+'day')
