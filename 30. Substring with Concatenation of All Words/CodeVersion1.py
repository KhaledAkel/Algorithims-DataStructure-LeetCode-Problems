class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        HashMap = {} # Set for saving the words appeared while looping
        l = 0
        result =[]
        for word in words:
            if word not in HashMap.keys():
                HashMap[word] = 0
            HashMap[word] += 1
        
        add = len(words[0])
        sub = add*len(words)
        if len(s) < 0:
            return []
        if len(s) == 1 and len(words) == 1:
            return [0]

        for i in range(len(s)-add):
            word = s[i:i+add]
            if word in HashMap.keys():
                copy = HashMap.copy()
                l = i
                while word in copy.keys() and l <= len(s)-add:
                    if copy[word] > 0:
                        copy[word]-=1
                    if copy[word] == 0:
                        del copy[word]
                    if not copy:
                        result.append(i)
                    l += add
                    word = s[l:l+add]
        return result
