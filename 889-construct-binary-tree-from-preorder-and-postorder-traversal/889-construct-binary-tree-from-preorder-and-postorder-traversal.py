
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        postorder_dict = {}

        for i, p in enumerate(postorder):
            postorder_dict[p] = i

        index = 0

        n = len(preorder)

        def construct(left, right):

            nonlocal index
            nonlocal postorder_dict

            if left > right:
                return None

            postorder_index = postorder_dict[preorder[index]]

            root = TreeNode(preorder[index])

            index += 1

            if index < n:
                next_preorder_val = preorder[index]
                next_postorder_index = postorder_dict[next_preorder_val]

                if postorder_index > next_postorder_index:
                    root.left = construct(left, next_postorder_index)
                    root.right = construct(next_postorder_index + 1, postorder_index - 1)

            return root

        res = construct(0, n - 1)
        
        return res