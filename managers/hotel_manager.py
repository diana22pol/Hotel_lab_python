"""
Importing of classes for manager
"""
# pylint: disable = import-error
from models.beach_hotel import BeachHotel
from models.motel import Motel
from models.mountain_hotel import MountainHotel
from models.resort_hotel import ResortHotel


class HotelManager:
    """
    A Class HotelManager that represents a manager of hotels
    """
    hotels = []

    def add_hotel(self, hotel):
        """
        Add a hotel to the hotel list.

        Args:
            hotel: An instance of the Hotel class or its subclasses.
        """
        self.hotels.append(hotel)

    def find_hotels_with_total_rooms_greater_than(self, total_rooms):
        """
        Find hotels with a total number of rooms greater than the specified value.

        Args:
            total_rooms: An integer representing the minimum total number of rooms.

        Returns:
            A list of hotel names that have a total
            number of rooms greater than the specified value.
        """
        return [hotel.name for hotel in self.hotels if hotel.total_rooms > total_rooms]

    def find_hotels_with_rating_greater_than(self, rating):
        """
        Find hotels with a rating greater than the specified value.

        Args:
            rating: A float representing the minimum rating.

        Returns:
            A list of hotel names that have a rating greater than the specified value.
        """
        return [hotel.name for hotel in self.hotels if hotel.rating > rating]

    @staticmethod
    def main():
        """
        The main method of the HotelManager class.
        Creates instances of different types of hotels, adds them to the hotel manager,
        and performs some operations on the hotel list.
        """
        manager = HotelManager()
        manager.add_hotel(Motel("Highway Motel", 30, 25, 3, "M4", "280 km", "Kyiv-Lviv"))
        manager.add_hotel(Motel("Highway Motel", 50, 25, 3, "M4", "280 km", "Kyiv-Lviv"))
        manager.add_hotel(ResortHotel("Beach Resort", 300, 150, 4, 2, 1, 7))
        manager.add_hotel(ResortHotel("Grand Resort", 500, 200, 5, 3, 2, 10))
        manager.add_hotel(BeachHotel("Marriott", 150, 62, 4, True))
        manager.add_hotel(BeachHotel("Hilton", 80, 22, 3, False))
        manager.add_hotel(MountainHotel("Winter holidays", 488, 70, 5, True))
        manager.add_hotel(MountainHotel("Ice Crystal Ski Resort", 656, 14, 5, True))

        for hotel in manager.hotels:
            print(str(hotel))

        print("\nHotels with total rooms greater than 200:")
        print(manager.find_hotels_with_total_rooms_greater_than(200))
        print("\nHotels with rating greater than 4:")
        print(manager.find_hotels_with_rating_greater_than(4))


HotelManager.main()
