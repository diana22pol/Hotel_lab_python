"""
Importing Hotel class
"""
# pylint: disable = import-error
from models.hotel import Hotel


class MountainHotel(Hotel):
    """
    A class used to represent a MountainHotel
    """
    # pylint: disable = too-many-arguments
    def __init__(self, name: str,
                 total_rooms: int,
                 available_rooms: int,
                 rating: float,
                 ski_lodge: bool):
        """
        Initializes a Hotel object.

        Parameters:
        name (str): The name of the hotel.
        total_rooms (int): The total number of rooms in the hotel.
        available_rooms (int): The number of available rooms in the hotel.
        rating (float): The rating of the hotel.
        ski_lodge (bool): Indicates whether the hotel has a ski lodge or not.
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.ski_lodge = ski_lodge
        self.working_days = {"St", "Tu", "Fr"}

    def get_location(self):
        """
        Returns None as the location of the hotel is not defined.
        """
        return None

    def __str__(self):
        """
        Returns a string representation of the Hotel object.

        Returns:
        str: A formatted string containing information about
            the hotel, including its name, total rooms,
            available rooms, rating, and ski lodge availability.
        """
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Ski Lodge: {self.ski_lodge}"
