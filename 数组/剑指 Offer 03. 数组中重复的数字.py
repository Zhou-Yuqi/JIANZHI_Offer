'''
剑指 Offer 03. 数组中重复的数字
简单

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
'''
# 哈希表
class Solution(object): 
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {} #初始化哈希表，key用于存储出现的数字、value用于存储该数字出现的次数
        for i in range(len(nums)): # 开始遍历nums中的每个数字
            if nums[i] in hash: # 如果当前位置下的值，是hash中的key
                return nums[i] # 说明重复了，返回这个值即可
            else:
                hash[nums[i]] = 1 # 给hash中插入新key和次数1

# 排序后比较
class Solution(object):
    def findRepeatNumber(self, nums):
        nums.sort() # 内置排序，从小到大
        for i in range(0, len(nums)-1): # 开始遍历nums
            if nums[i] == nums[i+1]: # 如果当前的和后面的一样
                return nums[i] # 说明重复了，返回这个值即可
        return -1 # 如果没有，那就返回-1哈