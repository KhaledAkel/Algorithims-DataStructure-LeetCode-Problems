class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        def dfs(word_index, i, j):
            if word_index == len(word):
                return True
            
            if (i<0 or i>= len(board) or 
                j<0 or j>=len(board[0]) or
                board[i][j] != word[word_index]):
                return False
            
            temp = board[i][j]
            board[i][j] = "#"

            exist = dfs(word_index+1, i-1, j) or dfs(word_index+1, i+1, j) or\
                    dfs(word_index+1, i, j-1) or dfs(word_index+1, i, j+1)

            board[i][j] = temp
            return exist
        
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                if dfs(0, i, j):
                    return True
        return False


        
