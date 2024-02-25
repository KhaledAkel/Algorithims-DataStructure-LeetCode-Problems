class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(root, preorderList):
            if not root:
                preorderList.append("None")
                return
            preorderList.append(str(root.val))
            preorder(root.left, preorderList)
            preorder(root.right, preorderList)

        preorderList = []
        preorder(root, preorderList)
        return ",".join(preorderList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(preorder):
            if preorder[0] == "None":
                preorder.pop(0)
                return None
            
            root_val = int(preorder.pop(0))
            root = TreeNode(root_val)
            root.left = dfs(preorder)
            root.right = dfs(preorder)
            return root

        preorder = data.split(",")
        return dfs(preorder)
