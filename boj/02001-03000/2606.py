m,n=int(input()),int(input())
d={i:[], for i in range(m)}
for i in range(n):
    a,b=map(int,input().split())
    d[a].add(b)
    d[b].add(a)
    print(d)





def vi(g, start):
    qu = []       # 기억 장소 1: 앞으로 처리해야 할 사람들을 큐에 저장
    done = set()  # 기억 장소 2: 이미 큐에 추가한 사람들을 집합에 기록(중복 방지)
    qu.append(start)    # 자신을 큐에 넣고 시작
    done.add(start)     # 집합에도 추가
    while qu:           # 큐에 처리할 사람이 남아 있는 동안
        p = qu.pop(0)   # 큐에서 처리 대상을 한 명 꺼내
        print(p)        # 이름을 출력하고
        for x in g[p]:  # 그의 친구들 중에
            if x not in done:  # 아직 큐에 추가된 적이 없는 사람을
                qu.append(x)   # 큐에 추가하고
                done.add(x)    # 집합에도 추가

vi(d,d[1])
