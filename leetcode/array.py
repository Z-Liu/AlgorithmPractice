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


# https://leetcode.com/problems/move-zeroes/description/
class Solution4(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp1 = temp2 = 0
        while temp1 < n and temp2 < n:
            while temp2 < n - 1 and nums[temp2] == 0:
                temp2 += 1
            nums[temp1], nums[temp2] = nums[temp2], nums[temp1]
            temp1 += 1
            temp2 += 1


# https://leetcode.com/problems/majority-element/description/
class Solution5(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ref_dict = {}
        n = len(nums)
        for i in nums:
            if i in ref_dict:
                ref_dict[i] += 1
            else:
                ref_dict[i] = 1
            if ref_dict[i] > (n / 2):
                return i


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
class Solution6(object):
    def maxProfit(self, prices):
        """
        :rtype: int
        """
        bottom_numbers = {}
        top_numbers = {}
        candidate = []
        n = len(prices)
        if n <= 1:
            return 0
        if prices[0] <= prices[1]:
            bottom_numbers[0] = prices[0]
        for i in range(1, n - 1):
            if prices[i - 1] >= prices[i] < prices[i + 1] or prices[i - 1] > prices[i] <= prices[i + 1]:
                bottom_numbers[i] = prices[i]
            if prices[i - 1] <= prices[i] > prices[i + 1] or prices[i - 1] < prices[i] >= prices[i + 1]:
                top_numbers[i] = prices[i]
        if prices[n - 2] < prices[n - 1]:
            top_numbers[n - 1] = prices[n - 1]
        if not bottom_numbers or not top_numbers:
            return 0
        for i in bottom_numbers:
            temp = [top_numbers[j] for j in top_numbers if j > i]
            if temp:
                candidate.append(max(temp) - bottom_numbers[i])
        return max(candidate)

    def maxProfit1(self, prices):
        import sys
        max_profit = 0
        min_price = sys.maxint
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_profit:
                max_profit = i - min_price
        return max_profit


if __name__ == '__main__':
    print Solution6().maxProfit1([7, 1, 5, 3, 6, 4])  # 5
    print Solution6().maxProfit1([1, 2])  # 1
    print Solution6().maxProfit1([])  # 0
    print Solution6().maxProfit1([7, 6, 4, 3, 1])
    print Solution6().maxProfit1([3, 2, 6, 5, 0, 3])
    print Solution6().maxProfit1([3, 4, 6, 0, 3, 7, 5, 8, 2, 9, 1, 6, 6, 2])
    print Solution6().maxProfit1([2, 2, 5])
    # print Solution5().majorityElement([1, 1, 1, 2])
    # print Solution5().majorityElement([1])
    # print Solution4().moveZeroes([0])
    # print Solution4().moveZeroes([1, 0])
    # print Solution4().moveZeroes([0, 1, 0, 3, 12])
# print Solution3().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])  # 5,6
# print Solution3().findDisappearedNumbers([1, 3, 2, 7, 8, 2, 3, 1])  # 4,5,6
# print Solution3().findDisappearedNumbers([1, 3, 2, 7, 8, 5, 5, 1])  # 4,6
# print Solution3().findDisappearedNumbers([3, 3, 3])
# print Solution3().findDisappearedNumbers([1, 1, 1])
# print Solution3().findDisappearedNumbers([2, 2, 2])
# print Solution1().removeDuplicates([0, 0])
# print Solution1().removeDuplicates([1, 1, 2, 2])
# print Solution1().removeDuplicates1([0, 0])
# print Solution1().removeDuplicates1([1, 1, 2, 2])
# print Solution().twoSum([3, 2, 4], 6)
# print Solution().twoSum1([3, 2, 4], 6)
# print Solution().twoSum2([3, 2, 4], 6)
