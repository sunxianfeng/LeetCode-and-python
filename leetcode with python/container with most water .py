# -*- coding:utf-8 -*-
def maxArea(height):
    len_height = len(height)
    if len_height == 1:
        return 0
    result,max_area = 0,0
    start = 0
    end = len_height - 1
    while start < end:
        max_area = min(height[start],height[end]) * (end - start)
        result = max(result, max_area)
        if height[start] <= height[end]: start += 1
        else: end -= 1
    return result
    # if height[left_index] < height[right_index]:
    #     area = (right_index - left_index) * height[left_index]
    #     left_index += 1
    # else:
    #     area = (right_index - left_index) * height[right_index]
    #     right_index -= 1
    # if area > max_area:
    #     max_area = area
height = [1,2,5,3,8,0,4,6,2]
res = maxArea(height)
print res