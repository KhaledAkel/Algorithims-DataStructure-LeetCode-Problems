class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):

            return False

        else:

            S = "".join(set(s))

            for x in S:

                if (s.count(x) != t.count(x)):

                    return False

            return True
