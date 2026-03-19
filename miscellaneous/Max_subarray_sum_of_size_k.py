t = int(input())

while(t):
    t-=1
    n,k = map(int, input().split())

    l = list(map(int, input().split()))

    i=0; j=k-1
    maxx, summ= 0,0
    for k in range(0,k):
        summ += l[k]
    
    maxx = summ


    while (j<n-1):

        j += 1
        summ = summ - l[i] + l[j]
        maxx = max(summ, maxx)
        i += 1

    print(maxx)