class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr=[]
        for num in nums:
            if num in arr:
                return False
            arr.append(num)
        return True