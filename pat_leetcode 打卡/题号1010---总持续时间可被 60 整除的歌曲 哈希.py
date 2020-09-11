##题目描述
# 输入：[30,20,150,100,40]
# 输出：3
# 解释：这三对的总持续时间可被 60 整数：
# (time[0] = 30, time[2] = 150): 总持续时间 180
# (time[1] = 20, time[3] = 100): 总持续时间 120
# (time[1] = 20, time[4] = 40): 总持续时间 60

"""
思路尝试
回归题意中的要求：和被 60 整除。我们分析满足条件的数字规律，20 + 40 可以，80 + 40 也可以，20 和 80 等效、其相同点是整除 60 后结果是相同的。所以，关键点来了，时间列表中每个数字可能差异极大，但对题目生效的只有该数整除 60 的余数结果：余数为 1 的和余数为 59 的组合必然满足题意要求。
拿到所有余数后，
其范围是 0 到 59。假设余数为 1 的有 10 个，余数为 59 的有 5 个，
那么我们可以算出它们可以生成 105 = 50 对有效结果；但这里特殊的是余数为 0 和 30 的，
假设余数为 30 的数字有 10 个，那么产生的不重复有效结果为 109/2 = 45 对。
整理一遍思路：先对时间列表中元素每个都整除拿到余数，
对每个余数的个数进行一番统计，从统计结果出发，计算可以组合出 60 的结果个数
"""


"""
1. 首先拿到所有数字的余数，放入字典中
2.统计所有余数的个数
3.根据上边总结的规律得到结果
"""
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dic={}
        for i,j in enumerate(time):
            r=j%60
            dic.setdefault(r,0)##默认字典中如果没有这个键，则值为0
            dic[r]+=1

        count=0#统计符合条件组数

        for i in range(31):
            if i in [0,30]:
                num=dic.get(i)##得到余数的个数
                if num and num>1:
                    count+=num*(num-1)//2
            else:
                num1=dic.get(i)
                num2=dic.get(60-i)
                if num1 and num2:
                    count+=num1*num2
        return count



def main():
    s=Solution()
    time=[20,40,60]
    res=s.numPairsDivisibleBy60(time)
    print(res)



if __name__=='__main__':#入口
    main()



