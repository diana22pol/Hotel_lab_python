"""
Parent abstract class Hotel
"""
from abc import ABC, abstractmethod


class Hotel(ABC):
    """
    Represents a hotel with its name, number of total rooms,
    number of available rooms and rating.
    """
    __instance = None

    def __init__(self, name="", total_rooms=None, available_rooms=None, rating=None):
        """
        Initializes a Hotel object.

        Parameters:
        name (str): The name of the hotel.
        total_rooms (int): The total number of rooms in the hotel.
        available_rooms (int): The number of available rooms in the hotel.
        rating (float): The rating of the hotel.
        """

        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms
        self.rating = rating

    def book_room(self):
        """
        Books a room in the hotel.
        """
        if self.available_rooms > 0:
            self.available_rooms -= 1

    def release_room(self):
        """
        Releases a room in the hotel.
        """
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1

    def get_available_rooms(self):
        """
        Returns the number of available rooms in the hotel.
        """
        return self.available_rooms

    def get_booked_rooms_count(self):
        """
        Returns the number of booked rooms in the hotel.
        """
        return self.total_rooms - self.available_rooms

    @abstractmethod
    def get_location(self):
        """
        Abstract method to get the location of the hotel.

        This method should be implemented by subclasses to
        provide the specific location information of the hotel.
        """

    @staticmethod
    def get_instance():
        """
        Returns a singleton instance of the Hotel class.
        """
        if not Hotel.__instance:
            Hotel.__instance = Hotel()
        return Hotel.__instance
