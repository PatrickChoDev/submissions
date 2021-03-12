t = int(input())
ans = [(0,0)]*t
for c in range(t):
    n,k = [int(x) for x in input().split()]

    l1 = sorted([int(x) for x in input().split()])
    l2 = sorted([int(x) for x in input().split()])
    print(l1,l2)
    imin ,imax = 0,0

    for i in range(k):
        imin += l1[i]*l2[i]
        imax += l1[::-1][i]*l2[::-1][i]
        print( l1[::-1][i],l2[::-1][i],end=' ')
    ans[c]=(imin,imax)

print("\n".join([str('Case #'+str(x+1)+': '+str(b[0])+' '+str(b[1])) for x,b in enumerate(ans)]))

