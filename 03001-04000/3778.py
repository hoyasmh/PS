import sys
for i in range(int(input())):
    l=[[0]*26,[0]*26]
    for j in range(2):
        for k in sys.stdin.readline().strip():
            l[j][ord(k)-97]+=1
    print('Case #{}: {}'.format(i+1,sum([abs(l[0][i]-l[1][i]) for i in range(26)])))
