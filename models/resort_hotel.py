"""
importing Hotel abstract class
"""
# pylint: disable = import-error
from models.hotel import Hotel


class ResortHotel(Hotel):
    """
    Class ResortHotel that represents Resort Hotel
    """

    # pylint: disable = too-many-arguments
    def __init__(self, name, total_rooms,
                 available_rooms, rating,
                 child_pools, adult_pools, restaurants_number):
        """
        Initializes a ResortHotel object.

        Parameters:
        name (str): The name of the hotel.
        total_rooms (int): The total number of rooms in the hotel.
        available_rooms (int): The number of available rooms in the hotel.
        rating (float): The rating of the hotel.
        child_pools (int): The number of child pools in the resort hotel.
        adult_pools (int): The number of adult pools in the resort hotel.
        restaurants_number (int): The number of restaurants in the resort hotel.
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.child_pools = child_pools
        self.adult_pools = adult_pools
        self.restaurants_number = restaurants_number

    def get_location(self):
        """
        Returns the name of the hotel.
        """
        return self.name

    def __str__(self):
        """
        Returns a string representation of the Hotel object.

        Returns:
        str: A formatted string containing information
            about the hotel, including its name, total rooms,
            available rooms, rating, child pools, adult pools, and restaurants number.
        """
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Child Pools: {self.child_pools}, Adult Pools: {self.adult_pools}, " \
               f"Restaurants Number: {self.restaurants_number}"
