def sum_r(l):
    if len(l) == 0:
        return 0
    else:
        return l[0]+sum_r(l[1:])
    


lis = list(map(int,input().split()))
sums = sum_r(lis)
print(sums)
