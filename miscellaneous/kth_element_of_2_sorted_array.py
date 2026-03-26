class Solution:
    def kthElement(self, a, b, k):
        i, j = 0, 0
        n, m = len(a), len(b)
        l = []

        while( len(l) < k)  and (i<n) and (j<m) :
            if(a[i] < b[j]) :
                l.append(a[i])
                i+=1
            else:
                l.append(b[i])
                j+=1

        while ( len(l) < k ) :
            if(i<n):
                l.append(a[i])
                i+=1
            else:
                l.append(b[i])
                j+=1
                
        return l[k-1]