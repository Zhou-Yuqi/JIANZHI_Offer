'''
剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
简单

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

 

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
'''

# 前后双指针
class Solution(object): 
    def exchange(self, nums):
        left = 0
        right = len(nums) - 1 # 初始化前后双指针
        while left < right:
            if nums[left] % 2 == 0 and nums[right] % 2 == 1: # 如果left指向的是偶数，且right指向的是奇数
                #nums[left], nums[right] = nums[right], nums[left] # 交换
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

            elif nums[left] % 2 == 1: # 如果left指向的是奇数
                left += 1
            elif nums[right] % 2 == 0: # 如果right指向的是偶数
                right -= 1
        return nums