class Jar:
    """
    A class representing a cookie jar with a limited capacity.

    The Jar class allows you to deposit and withdraw cookies, and provides methods
    to check the current number of cookies and the jar's capacity.

    Attributes:
        capacity (int): The maximum number of cookies the jar can hold.
        size (int): The current number of cookies in the jar.

    Methods:
        __str__(): Returns a string representation of the jar, showing the current
                   number of cookies using the "🍪" emoji.
        deposit(n): Deposits `n` cookies into the jar, if it does not exceed the capacity.
        withdraw(n): Withdraws `n` cookies from the jar, if there are enough cookies available.

        Created On: 01-01-2005
        Author :@arvidon
    """

    def __init__(self, capacity=12):
        """
        Initializes a new jar with a specified capacity and zero cookies.

        Args:
            capacity (int): The maximum number of cookies the jar can hold. Default is 12.

        Raises:
            ValueError: If `capacity` is a negative number.
        """
        if capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        """
        Returns a string representation of the jar.

        The string consists of "🍪" emojis that represent the current number of cookies.

        Returns:
            str: A string showing the current number of cookies in the jar.
        """
        return "🍪" * self._cookies

    def deposit(self, n):
        """
        Deposits a specified number of cookies into the jar.

        Args:
            n (int): The number of cookies to deposit. Must be a positive integer.

        Raises:
            ValueError: If `n` is less than or equal to 0.
            ValueError: If depositing `n` cookies exceeds the jar's capacity.
        """
        if n <= 0:
            raise ValueError("Number of cookies to deposit must be positive")
        if self._cookies + n > self._capacity:
            raise ValueError("Exceeds jar's capacity")
        self._cookies += n

    def withdraw(self, n):
        """
        Withdraws a specified number of cookies from the jar.

        Args:
            n (int): The number of cookies to withdraw. Must be a positive integer.

        Raises:
            ValueError: If `n` is less than or equal to 0.
            ValueError: If there are not enough cookies in the jar to withdraw the specified number.
        """
        if n <= 0:
            raise ValueError("Number of cookies to withdraw must be positive")
        if self._cookies < n:
            raise ValueError("Not enough cookies in the jar")
        self._cookies -= n

    @property
    def capacity(self):
        """
        Returns the maximum capacity of the jar.

        Returns:
            int: The capacity of the jar.
        """
        return self._capacity

    @property
    def size(self):
        """
        Returns the current number of cookies in the jar.

        Returns:
            int: The current number of cookies.
        """
        return self._cookies
