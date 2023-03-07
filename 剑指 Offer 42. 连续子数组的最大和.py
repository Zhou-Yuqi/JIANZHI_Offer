'''
剑指 Offer 42. 连续子数组的最大和

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 
示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

# 同leetcode 53.最大子数组和

# 动态规划
class Solution:
    def maxSubArray(self, nums):
        if not nums: # 如果num是空的，返回最大值为0就好了
            return 0

        # 以下是正常情况，去找连续子数组的最大和
        # dp array
        dp = [0] * len(nums)
        # dp init
        dp[0] = nums[0]
        # 开始dp
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i]) # 如果nums[i]已经比过去的dp[i-1]再加上nums[i]还大，那就重新开始算最大值了
        # 其实dp存的就是dp算法一路搜寻过来的所有可能最大值
        return max(dp) # 返回dp最大的一个就好

# class Solution:
#     def maxSubArray(self, nums):

#         # dp array
#         dp = [0] * len(nums)
#         # dp init
#         dp[0] = nums[0]
        
#         # dp
#         for i in range(1, len(nums)):
#             # If current value nums[i] is already larger than dp[i-1]+nums[i],
#             # We will definitely restart this subarray.
#             # Because the current value is bigger enough to represent the rest
#             dp[i] = max(nums[i], dp[i-1]+nums[i])

#         return max(dp)