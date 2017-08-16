class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum1(self, nums, target):
        nums_dict = dict()
        for i, num in enumerate(nums):
            nums_dict[num] = i
        for i, num in enumerate(nums):
            if nums_dict.get(target - num) and i != nums_dict[target - num]:
                return [i, nums_dict[target - num]]

    def twoSum2(self, nums, target):
        nums_dict = dict()
        for i, num in enumerate(nums):
            if nums_dict.get(target - num) and i != nums_dict[target - num]:
                return [nums_dict[target - num], i]
            nums_dict[num] = i


if __name__ == '__main__':
    print Solution().twoSum([3, 2, 4], 6)
    print Solution().twoSum1([3, 2, 4], 6)
    print Solution().twoSum2([3, 2, 4], 6)
