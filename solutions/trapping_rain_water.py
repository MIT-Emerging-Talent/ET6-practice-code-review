#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def trap(height):
    """
    Calculates the amount of rainwater that can be trapped given an elevation map.

    Parameters:
        height (list[int]): A list of non-negative integers representing the elevation map, where the width of each bar is 1.
    Returns:
        int: The total amount of trapped rainwater.

    Logic:
        - Uses two pointers (left and right) to traverse the elevation map.
        - Tracks the maximum height to the left and right of each bar.
        - Accumulates water trapped based on the minimum of these maximum heights.

        Examples:
        >>> trap([0,1,0,2,1,0,1,3,2,1,2,1])
        6
        >>> trap([4,2,0,3,2,5])
        9
        >>> trap([1,0,2,1,0,1,3,2,1,2,1])
        6
        >>> trap([1, 2, 3, 4])
        0
        >>> trap([5, 4, 3, 2, 1])
        0
        >>> trap([3, 0, 0, 2, 0, 4])
        10

    """

    # Defensive assertions for input validation
    assert isinstance(height, list), "Input must be a list."
    assert all(
        isinstance(h, int) and h >= 0 for h in height
    ), "All elements must be non-negative integers."

    # If there are fewer than 3 elements, no water can be trapped.
    if not height or len(height) < 3:
        return 0

    # Initialize pointers and variables
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    # Traverse the list with two pointers
    while left < right:
        if height[left] < height[right]:
            # Move the left pointer and update the left_max
            left += 1
            left_max = max(left_max, height[left])
            # Calculate the trapped water at the current left position
            water += max(0, left_max - height[left])
        else:
            # Move the right pointer and update the right_max
            right -= 1
            right_max = max(right_max, height[right])
            # Calculate the trapped water at the current right position
            water += max(0, right_max - height[right])

    return water
