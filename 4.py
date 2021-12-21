def findMedianSortedArrays(nums1, nums2):
    nums = nums1 + nums2
    nums = sorted(nums)
    if len(nums) % 2:
        return nums[len(nums)//2]
    else:
        return (nums[len(nums)//2] + nums[len(nums)//2-1]) / 2
