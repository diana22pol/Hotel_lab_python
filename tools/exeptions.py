class RatingError(Exception):
    """
    Custom exception for invalid ratings.

    Attributes:
        rating (float): The invalid rating value.
        message (str): The error message.
    """

    def __init__(self, rating, message="Rating must be a number between 0 and 5"):
        """
        Initialize RatingError with the given rating and message.

        Args:
            rating (float): The invalid rating value.
            message (str): The error message.
        """
        self.rating = rating
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        Return a string representation of the RatingError.

        Returns:
            str: The string representation of the RatingError.
        """
        return f"{self.rating} -> {self.message}"


class TotalRoomsError(Exception):
    """
    Custom exception for invalid total rooms.

    Attributes:
        total_rooms (int): The invalid total rooms value.
        message (str): The error message.
    """

    def __init__(self, total_rooms, message="Total rooms must be a positive integer"):
        """
        Initialize TotalRoomsError with the given total rooms and message.

        Args:
            total_rooms (int): The invalid total rooms value.
            message (str): The error message.
        """
        self.total_rooms = total_rooms
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """
        Return a string representation of the TotalRoomsError.

        Returns:
            str: The string representation of the TotalRoomsError.
        """
        return f"{self.total_rooms} -> {self.message}"
