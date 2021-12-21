def moveZeroes(nums):
    s = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            s += 1
        else:
            nums[i - s] = nums[i]
            if s > 0:
                nums[i] = 0
