from collections import defaultdict

class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.

        Args:
            s (str): The input string.

        Returns:
            int: The length of the longest substring without repeating characters.

        Raises:
            ValueError: If the input is not a string.

        Examples:
            >>> Solution().lengthOfLongestSubstring("abcabcbb")
            3
            >>> Solution().lengthOfLongestSubstring("bbbbb")
            1
            >>> Solution().lengthOfLongestSubstring("")
            0
        """
        if not isinstance(s, str):
            raise ValueError("Input must be a string.")

        # Dictionary to track character counts in the current substring
        char_count = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):
            # Increment the count of the current character
            char_count[s[right]] += 1

            # If a duplicate character is found, adjust the left pointer
            while char_count[s[right]] > 1:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length
