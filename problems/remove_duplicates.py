class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for number in nums:
            smol_list = []
            if number not in smol_list:
                smol_list.append(number)
        return len(smol_list)