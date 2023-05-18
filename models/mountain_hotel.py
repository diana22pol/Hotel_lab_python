from models.hotel import Hotel

"""
Hotel subclass - MountainHotel
"""


class MountainHotel(Hotel):
    def __init__(self, name, total_rooms, available_rooms, rating, ski_lodge):
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

    def get_Location(self):
        """
        Returns None as the location of the hotel is not defined.
        """
        return None

    def __str__(self):
        """
        Returns a string representation of the Hotel object.

        Returns:
        str: A formatted string containing information about the hotel, including its name, total rooms,
             available rooms, rating, and ski lodge availability.
        """
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Ski Lodge: {self.ski_lodge}"

