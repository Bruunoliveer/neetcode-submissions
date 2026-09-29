class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = {}
        for num in nums:
            if num in test and test[num] is True:
                return True
            else:
                test[num] = True
        return False