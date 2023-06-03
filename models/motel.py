"""
Hotel subclass - Motel
"""
# pylint: disable = import-error
from models.hotel import Hotel


class Motel(Hotel):
    """
    A class Motel that represents Motel
    """
    # pylint: disable = too-many-arguments
    def __init__(self, name, total_rooms,
                 available_rooms, rating,
                 track_number_nearby, track_kilometers,
                 cities_nodes):
        """
        Initializes a Hotel object.

        Parameters:
        name (str): The name of the hotel.
        total_rooms (int): The total number of rooms in the hotel.
        available_rooms (int): The number of available rooms in the hotel.
        rating (float): The rating of the hotel.
        track_number_nearby (str): The track number nearby the hotel.
        track_kilometers (str): The distance of the track in kilometers.
        cities_nodes (str): The nodes of cities located near the hotel.
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.track_number_nearby = track_number_nearby
        self.track_kilometers = track_kilometers
        self.cities_nodes = cities_nodes
<<<<<<< HEAD
        self.working_days = {"Mo", "We", "Th"}

=======
>>>>>>> main

    def get_location(self):
        """
        Gets the location of the hotel.

        Returns a string representation of the hotel's location,
        including the cities nodes and track kilometers.
        """
        return self.cities_nodes + "\t" + self.track_kilometers

    def __str__(self):
        """
        Returns a string representation of the Hotel object.

        Returns:
        str: A formatted string containing
            information about the hotel, including its name, total rooms,
            available rooms, rating, track number nearby, track kilometers, and cities nodes.
        """
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Track Number Nearby: {self.track_number_nearby}, " \
               f"Track Kilometers: {self.track_kilometers}, " \
<<<<<<< HEAD
               f"Cities Nodes: {self.cities_nodes} – " \
               f"Cities Nodes: {self.working_days}"
=======
               f"Cities Nodes: {self.cities_nodes}"
>>>>>>> main
