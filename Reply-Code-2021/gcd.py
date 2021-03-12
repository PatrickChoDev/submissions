def find_gcd(x, y):
     
    while(y):
        x, y = y, x % y
     
    return x

c=[0]*20
for i in range(int(input())):
    num = int(input())
    l = [int(x) for x in input().split()]
    num1 = l[0]
    num2 = l[1]
    gcd = find_gcd(num1, num2)
    for x in range(2, len(l)):
        gcd = find_gcd(gcd, l[x])
    for y in range(1,gcd):
        if gcd%y==0:
            c[i]+=1

print("\n".join([str('Case #'+str(x+1)+': '+str(b+1)) for x,b in enumerate(c)]))