class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag=1
        for i in range( 0, len(s)-1):
            if ( (s[i]=='0') and (s[i+1]=='1') ):
                flag=0
                break
        
        if(flag==1):
            return True
        else:
            return False