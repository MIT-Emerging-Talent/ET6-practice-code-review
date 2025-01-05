def find_partitions(n, max_num):
    """
    Find all possible partitions of a number `n` using integers from 1 to `max_num`.

    A partition of `n` is a way of writing it as a sum of positive integers, where
    the order of terms doesn't matter. This function returns all unique partitions
    of `n` using numbers from 1 to `max_num`.

    Parameters:
    - n (int): The number to be partitioned.
    - max_num (int): The largest integer that can be used in the partition.

    Returns:
    - list of lists: A list containing all partitions, where each partition is a
      list of integers that sum to `n`. All numbers used are <= `max_num`.
    """
    # Base case: If n is negative or max_num is 0, return an empty list
    if n < 0 or max_num == 0:
        return []

    # Initialize a list for partitions that exactly match n
    exact_match = []

    # If n equals max_num, include the partition [max_num]
    if n == max_num:
        exact_match = [[max_num]]

    # Find partitions that include max_num by subtracting it from n
    with_max_num = [
        partition + [max_num] for partition in find_partitions(n - max_num, max_num)
    ]

    # Find partitions that exclude max_num by reducing max_num
    without_max_num = find_partitions(n, max_num - 1)

    # Return combined partitions: exact matches, with max_num, and without max_num
    return sorted(exact_match) + sorted(with_max_num) + sorted(without_max_num)


# Example usage: Find partitions of 6 using numbers from 1 to 4
print(find_partitions(6, 4))
