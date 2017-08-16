class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)

    def removeDuplicates1(self, nums):
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    print Solution().removeDuplicates([0, 0])
    print Solution().removeDuplicates([1, 1, 2, 2])
    print Solution().removeDuplicates1([0, 0])
    print Solution().removeDuplicates1([1, 1, 2, 2])
