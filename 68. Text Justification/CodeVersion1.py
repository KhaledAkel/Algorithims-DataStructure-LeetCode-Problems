class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output =[]
        lineWords = []
        charlen = 0
        for i in range(len(words)):
            if maxWidth-(charlen+len(words[i])) >= 0:
                lineWords += [words[i] +" "]
                charlen += len(words[i]) + 1
                    
            else:
                lineWords[-1] = lineWords[-1][:-1]
                charlen -=1
                spaces = maxWidth-charlen
                j = 0
                while charlen < maxWidth:
                    if j >= len(lineWords)-1:
                        j = 0
                    lineWords[j] += " "
                    charlen += 1
                    j += 1

                line = "".join(lineWords)
                output += [line]
                lineWords = [words[i] + " "]
                charlen = len(words[i])+1
            if i == len(words)-1:
                lineWords[-1] = lineWords[-1][:-1]
                charlen -=1
                for k in range(maxWidth-charlen):
                    lineWords[-1] += " "
                line = "".join(lineWords)
                output += [line]
                
        return output
