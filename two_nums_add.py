'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 方法1
# class Solution():
#     def two_nums_add(self,list_,tar):
#         index_list=[]
#         for i in range(len(list_)):
#             for j in range(i+1,len(list_)):
#                 if list_[i]+list_[j]==tar:
#                     index_list.append(i)
#                     index_list.append(j)
#
#
#
#         return index_list
#
#
# if __name__ == '__main__':
#     s=Solution()
#     print(s.two_nums_add([2,7,11,15],13))

# 方法二，用哈希表来以空间换区速度

class Solution:
    def two_nums(self,list_,tar):
        dict_num={}
        index_list=[]
        for i in range(len(list_)):
            num=tar-list_[i]
            if num not in dict_num:
                dict_num[list_[i]]=i

            else:
                index_list.append(dict_num[num])
                index_list.append(i)

        return index_list

if __name__ == '__main__':
    s=Solution()
    print(s.two_nums([2,7,11,15],9))
