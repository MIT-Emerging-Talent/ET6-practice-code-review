class Solution(object):
  def twoSum(self, nums, target):
    """
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

    Args:
    nums (List[int]): List of integers.
    target (int): The target sum.

    Returns:
    List[int]: Indices of the two numbers such that they add up to `target`.

    Example:
    >>> solution = Solution()
    >>> solution.twoSum([2, 7, 11, 15], 9)
    [0, 1]

    Note:
    - Each input would have exactly one solution.
    - You may not use the same element twice.
    """
    num_to_index = {}
    for index, num in enumerate(nums):
      complement = target - num
      if complement in num_to_index:
        return [num_to_index[complement], index]
      num_to_index[num] = index