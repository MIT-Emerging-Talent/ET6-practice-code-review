def find_partitions(n, max_num):
    """
    Finds all possible partitions of a number `n` using numbers from 1 to `max_num`.

    A partition of a number is a way of writing it as the sum of positive integers,
    where the order of the terms does not matter. This function finds all the distinct
    ways to partition `n` using numbers from `1` to `max_num`.

    Parameters:
    - n (int): The number to be partitioned.
    - max_num (int): The largest integer that can be used in the partition.

    Returns:
    - list of lists: A list of partitions, where each partition is a list of integers.
      Each partition is a unique combination of numbers summing to `n`, and all numbers
      used in the partition are <= `max_num`.
    """
    # Base case: if n is negative or max_num is 0, return an empty list
    if n < 0 or max_num == 0:
        return []

    # Initialize a list to store partitions that exactly match n
    exact_match = []

    # If n is exactly equal to max_num, include the partition [max_num]
    if n == max_num:
        exact_match = [[max_num]]

    # Recursively find partitions that include max_num
    with_max_num = [
        partition + [max_num] for partition in find_partitions(n - max_num, max_num)
    ]

    # Recursively find partitions that exclude max_num, using smaller numbers
    without_max_num = find_partitions(n, max_num - 1)

    # Return the combined list of partitions:
    # - exact matches
    # - partitions with max_num included
    # - partitions without max_num included
    return sorted(exact_match) + sorted(with_max_num) + sorted(without_max_num)


# Example: Find partitions of 6 using numbers from 1 to 4
print(find_partitions(6, 4))
