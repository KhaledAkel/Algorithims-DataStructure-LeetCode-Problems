class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            copy = str(sorted(word))
            if copy in hashMap.keys():
                hashMap[copy].append(word)
            else:
                hashMap[copy] = [word]
        
        res=[]
        for lis in hashMap.values():
            res.append(lis)
        
        return res






        
