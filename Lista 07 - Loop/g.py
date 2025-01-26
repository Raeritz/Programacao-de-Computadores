n = int(input())
xlist = list(map(int, input().split()))
media = sum(xlist) / n
abmedia = []
igacmedia = []
for numero in xlist:
    if numero < media:
        abmedia.append(numero)
    else:
        igacmedia.append(numero)
print(f"{media:.1f}")
print(len(abmedia), * abmedia)
print(len(igacmedia), * igacmedia)