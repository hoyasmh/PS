s=input()
n=len(s)
l=['.#...#...*..'*5,'#.#.#.#.*.*.'*5,'.{}.#.{}.*.{}.*'*5]
for i in range(5):
    print('#'+l[2][:n*5-1].format(*list(s))+'#*'[n%3==0] if i==2 else '.'+l[min(i,4-i)][:4*n])
    # if i==2:
    #     print('#'+l[2][:len(s)*5-1].format(*list(s))+'#*'[len(s)%3==0])
    # else:
    #     print('.'+l[min(i,4-i)][:4*len(s)])
