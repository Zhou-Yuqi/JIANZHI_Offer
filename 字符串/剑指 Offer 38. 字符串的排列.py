'''
剑指 Offer 38. 字符串的排列
中等

输入一个字符串，打印出该字符串中字符的所有排列。

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
 
'''

class Solution(object): #分治法

    def permutation_func(self, s): 
        if len(s) == 1: #如果长度为1
            return s[0] #直接返回就行

        res = [] # 初始化返回的list

        for i in range(len(s)): # 遍历长度，即遍历mid位置i
            mid_res = self.permutation_func(s[:i] + s[i+1:]) # 除了i位置之外，其余两部分拼在一起，去找排列
            for j in mid_res: # mid_res里的排列，遍历每一个
                res.append(s[i] + j) # 把i位置的元素，和每一个拼在一起
        return res # 返回res，这里面可能有重复的哈

    def permutation(self, ss):
        if not ss:
            return []

        list_s = list(ss) # str转为list，每一个str是一个元素

        # 由于调用分治法premutation_func后返回的结果会有重复值，
        # 所以需要先set集合，去重
        # 再排序
        # 再用list将set转换回list，以返回
        return list(sorted(set(self.permutation_func(list_s))))