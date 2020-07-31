class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banset = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        proc = paragraph.split()
        for i in proc:
            i = i.lower()
        hashmap = {} 
        for i in proc:
            if i.lower() not in banned:
                if i.lower() in hashmap:
                    hashmap[i.lower()] += 1
                else:
                    hashmap[i.lower()] = 1

        return max(hashmap, key=hashmap.get)
                    
                    
            
            
            
        