n = int(input())
for x in range(n):
    if  n/n == 1:
        print("Sim")
    else:
        print("Nao")

==================================

n = int(input())
if n < 2:
    print("Nao")
else:
    primo = True
    
    for x in range(2, n):
        if x * x > n:
            break
        if n % x == 0:
            primo = False
            break
    if primo:
        print("Sim")
    else:
        print("Nao")