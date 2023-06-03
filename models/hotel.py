"""
<<<<<<< HEAD
<<<<<<<< HEAD:models/hotel.py
Parent abstract class Hotel
========
Lab 1 model for class Hotel
>>>>>>>> main:hotel.py
=======
Parent abstract class Hotel
>>>>>>> main
"""
from abc import ABC, abstractmethod


class Hotel(ABC):
    """
<<<<<<< HEAD
    Represents a hotel with its name, number of total rooms, number of available rooms and rating.
=======
    Represents a hotel with its name, number of total rooms,
    number of available rooms and rating.
>>>>>>> main
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
<<<<<<< HEAD
<<<<<<<< HEAD:models/hotel.py
=======
>>>>>>> main

        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms
        self.rating = rating
<<<<<<< HEAD
        self.working_days = set()

    def __iter__(self):
        return iter(self.working_days)
========
        self._name = name
        self._total_rooms = total_rooms
        self._available_rooms = available_rooms
        self._rating = rating
>>>>>>>> main:hotel.py
=======
>>>>>>> main

    def book_room(self):
        """
        Books a room in the hotel.
        """
<<<<<<< HEAD
        if self._available_rooms > 0:
            self._available_rooms -= 1
=======
        if self.available_rooms > 0:
            self.available_rooms -= 1
>>>>>>> main

    def release_room(self):
        """
        Releases a room in the hotel.
        """
<<<<<<< HEAD
        if self._available_rooms < self._total_rooms:
            self._available_rooms += 1
=======
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1
>>>>>>> main

    def get_available_rooms(self):
        """
        Returns the number of available rooms in the hotel.
        """
<<<<<<< HEAD
        return self._available_rooms
=======
        return self.available_rooms
>>>>>>> main

    def get_booked_rooms_count(self):
        """
        Returns the number of booked rooms in the hotel.
        """
<<<<<<< HEAD
        return self._total_rooms - self._available_rooms
=======
        return self.total_rooms - self.available_rooms
>>>>>>> main

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
<<<<<<< HEAD
<<<<<<<< HEAD:models/hotel.py
========


if __name__ == '__main__':
    hotels = [
        Hotel(),
        Hotel("Grand Hotel", 50, 10, 4),
        Hotel.get_instance(),
        Hotel.get_instance()
    ]

    for hotel in hotels:
        print(
            f"Hotel: {hotel._name}, Total Rooms: {hotel._total_rooms}, Available Rooms: {hotel._available_rooms}, "
            f"Rating: {hotel._rating}")
>>>>>>>> main:hotel.py
=======
>>>>>>> main
