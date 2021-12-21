def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        req = target - nums[i]
        if req in d:
            return [d[req], i]
        else:
            d[nums[i]] = i
