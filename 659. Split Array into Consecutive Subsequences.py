## time - O(n), space - O(1)
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        if not nums:
            return False
        i = 0
        pre = None
        lenCnt = [0] * 3
        while i < len(nums):
            tmp = [i for i in lenCnt]
            curr = nums[i]
            cnt = 0
            while i < len(nums) and nums[i] == curr:
                cnt += 1
                i += 1

            if pre == None:
                lenCnt[0] = cnt
            elif pre == curr - 1:
                if cnt < lenCnt[0] + lenCnt[1]:
                    return False
                lenCnt[0] = max(0, cnt - sum(tmp))
                lenCnt[1] = tmp[0]
                lenCnt[2] = tmp[1] + min(tmp[2], cnt - tmp[0] - tmp[1])
            else:
                if lenCnt[0] or lenCnt[1]:
                    return False
                lenCnt[2] = 0
                lenCnt[0] = cnt
            pre = curr

        if lenCnt[0] or lenCnt[1]:
            return False
        else:
            return True



## sol2
from collections import defaultdict, deque


class Solution(object)2:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        num_length = defaultdict(deque)

        for num in nums:
            if num - 1 not in num_length:
                num_length[num].append(1)
            else:
                length = num_length[num - 1].pop()
                if len(num_length[num - 1]) == 0:
                    del num_length[num - 1]
                if length + 1 >= 3:
                    num_length[num].appendleft(length + 1)
                else:
                    num_length[num].append(length + 1)

        for num, length in num_length.items():
            for l in length:
                if l < 3:
                    return False
        return True