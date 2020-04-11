## time - O(n), space - O(logn)
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if right < left:
                return None
            mid = left + (right - left + 1) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)