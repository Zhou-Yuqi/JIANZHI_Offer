'''
剑指 Offer 40. 最小的k个数
简单

输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
'''

# 快速排序
# class Solution(object):
#     def getLeastNumbers(self, arr, k):
#         """
#         :type arr: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         def quick_sort(arr, l, r):
#             # 【注意】这条很重要，需要判断左右子数组长度是否为1。
#             # 如果用l==r，或者len(arr[l:r])==0，后面索引切片的时候都会报错。。。
#             # 必须用这个，如果左指针大于等于右指针，才行哈。。
#             if l >= r: return  # 判断：子数组长度为 1 时终止递归
            
#             i, j = l, r # 初始化左右指针
#             while i < j: # 只要左指针小于右指针，执行
#                 while i < j and arr[j] >= arr[l]: # 从右向左找，找到第一个小于哨兵值arr[l]的位置
#                     j -= 1
#                 while i < j and arr[i] <= arr[l]: # 从左向右找，找到第一个大于哨兵值arr[l]的位置
#                     i += 1
#                 arr[i], arr[j] = arr[j], arr[i] # 交换
#             arr[l], arr[i] = arr[i], arr[l] # 交换，得到新的哨兵值
#             quick_sort(arr, l, i - 1) # 递归，排序左子数组
#             quick_sort(arr, i + 1, r) # 递归，排序右子数组
#             return arr
        
#         arr_ = quick_sort(arr, 0, len(arr)-1)
#         return arr[:k]
    

# 堆
'''
用一个大根堆实时维护数组的前 k 小值。
首先将前 k 个数插入大根堆中，随后从第 k+1 个数开始遍历，
如果当前遍历到的数比大根堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数。
最后将大根堆里的数存入数组返回即可

【注意】Python 语言中的堆为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值。
'''
class Solution:
    def getLeastNumbers(self, arr, k):
        import heapq
        if k == 0:
            return list()

        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


s = Solution()
re = s.getLeastNumbers(arr = [2,4,1,0,3,5], k = 2)
print(re)