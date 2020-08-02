class Solution:
    def generate(self, numRows):
        accum = []
        for i in range(0,numRows):
            if i == 0:
                accum.append([1])
            if i == 1:
                accum.append([1,1])
            if i != 0 and i != 1:
                inner = []
                prev = accum[len(accum)-1]
                for j in range(0,len(prev)-1):
                    inner.append(prev[j]+prev[j+1])
                inner.insert(0,1)
                inner.insert(len(inner),1)
                accum.append(inner)
        return accum
                
            
        
Solution().generate(10)