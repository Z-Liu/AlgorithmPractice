# https://leetcode.com/problems/two-sum/description/
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


# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
class Solution1(object):
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


# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution3(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def exchange(arr, current_num, current_pos):
            if arr[current_num - 1] != arr[current_pos]:
                arr[current_num - 1], arr[current_pos] = arr[current_pos], arr[current_num - 1]
                current_num = arr[current_pos]
                exchange(arr, current_num, current_pos)
            else:
                return

        n = len(nums)
        i = 0
        while i < n:
            exchange(nums, nums[i], i)
            i += 1
        res = []
        for i in range(len(nums)):
            if i != nums[i] - 1:
                res.append(i + 1)
        return res


if __name__ == '__main__':
    print Solution3().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])  # 5,6
    print Solution3().findDisappearedNumbers([1, 3, 2, 7, 8, 2, 3, 1])  # 4,5,6
    print Solution3().findDisappearedNumbers([1, 3, 2, 7, 8, 5, 5, 1])  # 4,6
    print Solution3().findDisappearedNumbers([3, 3, 3])
    print Solution3().findDisappearedNumbers([1, 1, 1])
    print Solution3().findDisappearedNumbers([2, 2, 2])
    # print Solution1().removeDuplicates([0, 0])
    # print Solution1().removeDuplicates([1, 1, 2, 2])
    # print Solution1().removeDuplicates1([0, 0])
    # print Solution1().removeDuplicates1([1, 1, 2, 2])
    # print Solution().twoSum([3, 2, 4], 6)
    # print Solution().twoSum1([3, 2, 4], 6)
    # print Solution().twoSum2([3, 2, 4], 6)
