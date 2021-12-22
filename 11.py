def maxArea(self, height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    m_a = 0
    while l < r:
        a = (r - l) * min(height[l], height[r])
        if a > m_a:
            m_a = a
        if height[l] > height[r]:
            r -= 1
        elif height[l] < height[r]:
            l += 1
        else:
            l += 1
            r -= 1
    return m_a
