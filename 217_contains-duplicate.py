class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        list_length = len(nums)
        set_nums = set(nums)
        set_length = len(set_nums)

        res = True

        if list_length == set_length:
            return not res
        else:
            return res


type_nums = list([1, 2, 3, 1])

new_solution = Solution()
new_solution.containsDuplicate(type_nums)

