class Solution:
    def findTwoElement( self,a): 
        s = set()
        missing =0
        duplicate = 0
        
        for i in a:
            if i in s:
                duplicate = i
                
            else:
                s.add(i)
        
        for i in range(1,max(a)+1):
            if i in s:
                continue
            else:
                missing = i
        if missing==0:
            missing = max(a)+1
        
        return [duplicate,missing]