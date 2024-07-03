class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        def RLE(input_str):
            count = 1
            out = ""
            for i in range(1, len(input_str)):
                if input_str[i] == input_str[i-1]:
                    count += 1
                else:
                    out += str(count)
                    out += input_str[i-1]
                    count = 1

            out += str(count)
            out += input_str[-1]
            return out

        out = "1"
        for _ in range(n-1):
            out = RLE(out)

        return out 
