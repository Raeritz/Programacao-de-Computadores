z = int(input())
a, b, c, d= map(int,input().split)

#Primeira linha output
y = z//1
print(f"{y:.1f}")
#Segunda linha output
print()
#Terceira linha output

================================================
n = int(input())
xlist = list(map(int, input().split()))
media = sum(xlist) / n
abmedia = 0
igacmedia = 0
for numero in xlist:
    if numero < media:
        abmedia += 1
    else:
        igacmedia += 1
print(f"{media:.1f}")
print(abmedia)
print(igacmedia)



