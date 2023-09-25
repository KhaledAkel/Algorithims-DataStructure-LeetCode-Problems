class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]

        HashMap = dict()
        output = []

        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))  # Convert the sorted list of characters back to a string
            if word in HashMap:
                HashMap[word].append(strs[i])
            else:
                HashMap[word] = [strs[i]]

        for i in HashMap:
            output.append(HashMap[i])

        return output
