s=[10]
l=[1]*10
for i in range(1000):
    l=[l[1]+l[3],l[0]+l[2]+l[4],l[1]+l[5],l[0]+l[4]+l[6],l[1]+l[3]+l[5]+l[7],l[2]+l[4]+l[8],l[3]+l[7]+l[9],l[4]+l[6]+l[8],l[5]+l[7],l[6]]
    s.append(sum(l)%1234567)
for i in range(int(input())):
    print(s[int(input())-1])
