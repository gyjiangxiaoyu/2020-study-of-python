# 给你一个整数数组 arr 和两个整数 k 和 threshold 。
#
# 请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
#
#  
#
# 示例 1：
#
# 输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# 输出：3
# 解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
# 示例 2：
#
# 输入：arr = [1,1,1,1,1], k = 1, threshold = 0
# 输出：5
# 示例 3：
#
# 输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# 输出：6
# 解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
# 示例 4：
#
# 输入：arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
# 输出：1
# 示例 5：
#
# 输入：arr = [4,4,4,4], k = 4, threshold = 1
# 输出：1



class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        res=[0]
        ans=0#计数器
        for i in range(len(arr)):
            res.append(res[-1] + arr[i])###得到的是[0,1,3,6]

        for j in range(len(res)-k):
            b=res[j+k]##窗口汇总函数
            a=res[j]
            if (b-a)/k>=threshold:
                ans+=1
        return ans





def main():
    arr=[1,2,3]
    k=1
    threshold=2
    s=Solution()
    result=s.numOfSubarrays(arr,k,threshold)
    print(result)


if __name__=="__main__":
    main()


