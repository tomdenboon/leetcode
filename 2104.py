def subArrayRanges(nums):
    t_sum = 0
    for i in range(len(nums)):
        debug = []
        debug.append(nums[i])
        low = nums[i]
        high = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] < low:
                low = nums[j]
            if nums[j] > high:
                high = nums[j]
            debug.append(nums[j])
            t_sum += high - low
    return t_sum
