class Solution:
    def max_area(self, height):
        """
        Calculates the maximum area of water a container can hold.

        Args:
            height (List[int]): A list of non-negative integers representing the height of walls.

        Returns:
            int: The maximum area of water that can be contained.

        Raises:
            ValueError: If the input is not a list of non-negative integers.

        Examples:
            >>> Solution().maxArea([1,8,6,2,5,4,8,3,7])
            49
            >>> Solution().maxArea([1,1])
            1
            >>> Solution().maxArea([4,3,2,1,4])
            16
        """
        # Input validation
        if not isinstance(height, list) or not all(
            isinstance(h, int) and h >= 0 for h in height
        ):
            raise ValueError("Input must be a list of non-negative integers.")

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate area with the current left and right pointers
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
