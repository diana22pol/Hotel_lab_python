"""
Hotel subclass - BeachHotel
"""
# pylint: disable = import-error
from models.hotel import Hotel


class BeachHotel(Hotel):
    """
    Class BeachHotel that represents Beach Hotel
    """
    # pylint: disable = too-many-arguments
    def __init__(self, name, total_rooms, available_rooms, rating, beach_front):
        """
        Initializes a Hotel object.

        Parameters:
        name (str): The name of the hotel.
        total_rooms (int): The total number of rooms in the hotel.
        available_rooms (int): The number of available rooms in the hotel.
        rating (float): The rating of the hotel.
        beach_front (bool): Indicates whether the hotel is located on the beach front or not.
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.beach_front = beach_front

    def get_location(self):
        """
        Returns None as the location of the hotel is not defined.
        """
        return None

    def __str__(self):
        """
        Returns a string representation of the Hotel object.

        Returns:
        str: A formatted string containing information
             about the hotel, including its name, total rooms,
             available rooms, rating, and beachfront availability.
        """
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Beach Front: {self.beach_front}"
