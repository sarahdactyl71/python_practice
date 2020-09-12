def rotate(self, nums, k):
    return nums[k:] + nums[:k]