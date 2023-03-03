'''
剑指 Offer 11. 旋转数组的最小数字
简单

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。
请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。  

注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

 

示例 1：

输入：numbers = [3,4,5,1,2]
输出：1
示例 2：

输入：numbers = [2,2,2,0,1]
输出：0
'''

class Solution(object): # 二分查找法
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        N = len(numbers)
        left, right = 0, N - 1 # 定义左指针右指针
        while left < right: # 如果满足左指针小于右指针
            mid = (left + right) // 2 # 计算中间的指针
            if numbers[mid] < numbers[right]: # 如果mid的值比right的值小，说明mid一定在右边这个数组里
                right = mid
            elif numbers[mid] > numbers[right]: # 如果mid的值比right的值要大，那就说明，mid应该在左边那个数组里
                left = mid + 1
            else: # 如果mid的值和right的值相同
                right = right - 1 # right往左移一个。【关键所在!】可以证明这样操作，不会丢失最小值。（1、设right是唯一的最小值，那就不可能满足numbers[left]=numbers[right]；2、设right不是唯一的最小值，而又有numbers[left]=numbers[right]，说明left+1到right里面肯定还有很多个最小值），因此可以证明不会丢失最小值。
        
        # 直到while条件不满足，即left和right指针重叠了
        # 那就说明找到切分点了
        return numbers[left] #随便返回left或者right的即可哈