class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        Tset= set(zip(s, t))
        return len(Tset) == len(set(s)) == len(set(t))
