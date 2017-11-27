# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums) <= 1:
#         return len(nums)
#     slow = 0
#     for fast in xrange(1, len(nums)):
#         if nums[fast] != nums[slow]:
#             slow += 1
#             nums[slow] = nums[fast]
#     return slow + 1
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 2:
        return len(nums)
    cnt = 0
    j = 1
    for i in xrange(1, len(nums)):
        if nums[i] == nums[i - 1]:
            cnt += 1
            if cnt < 2:
                nums[j] = nums[i]
                j += 1
        else:
            nums[j] = nums[i]
            j += 1
            cnt = 0
    return j
print removeDuplicates([1,1,1,2,2,3])