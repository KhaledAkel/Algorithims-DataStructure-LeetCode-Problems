class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = collections.defaultdict(list)
        for word in strs:
            letters = [0]*26
            for letter in word:
                letters[ord(letter) - ord('a')] += 1
            hashMap[tuple(letters)].append(word)
        return hashMap.values()

        
