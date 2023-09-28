class Solution:
    def compress(self, chars: List[str]) -> int:
        
        pos = 0
        count = 1

        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count == 1:
                    chars[pos] = chars[i-1]
                    pos += 1
                else:
                    chars[pos] = chars[i-1]
                    pos += 1
                    for ele in str(count):
                        chars[pos] = ele
                        pos +=1
                    count = 1
        if count > 1:
            chars[pos] = chars[-1]
            pos += 1
            for ele in str(count):
                chars[pos] = ele
                pos += 1
        else:
            chars[pos] = chars[-1]
            pos += 1

        return pos





        
