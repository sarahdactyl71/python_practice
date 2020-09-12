def removeDuplicates(self, nums):
    for number in nums:
        smol_list = []
        if number not in smol_list:
            smol_list.append(number)
    return len(smol_list)

  #optionally, we can use a set
  #return len(list(set(nums)))
