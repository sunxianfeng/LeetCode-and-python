def trap(height):
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        if height[l] <= height[r]:
            if height[l + 1] < height[l]:
                ans += height[l] - height[l + 1]
                height[l + 1] = height[l]
            l = l + 1
        else:
            if height[r - 1] < height[r]:
                ans += height[r] - height[r - 1]
                height[r - 1] = height[r]
            r = r - 1
    return ans
print trap([0,1,0,2,1,0,1,3,2,1,2,1])