"""
Importing of classes for manager
"""
# pylint: disable = import-error
from models.beach_hotel import BeachHotel
from models.motel import Motel
from models.mountain_hotel import MountainHotel
from models.resort_hotel import ResortHotel
import re
import datetime


class HotelManager:
    """
    A Class HotelManager that represents a manager of hotels
    """
    hotels = []

    def log_calls(filename):
        def decorator(func):
            def wrapper(*args, **kwargs):
                with open(filename, 'a') as f:
                    f.write(f"{func.__name__} called at {datetime.datetime.now()}\n")
                return func(*args, **kwargs)

            return wrapper

        return decorator

    def enforce_snake_case(func):
        def wrapper(*args, **kwargs):
            if not re.match(r'^[a-z]+(_[a-z]+)*$', func.__name__):
                raise Exception(f"Method name '{func.__name__}' is not written in snake_case")
            return func(*args, **kwargs)

        return wrapper

    @enforce_snake_case
    @log_calls("./log.txt")
    def add_hotel(self, hotel):
        """
        Add a hotel to the hotel list.

        Args:
            hotel: An instance of the Hotel class or its subclasses.
        """
        self.hotels.append(hotel)

    @enforce_snake_case
    @log_calls("./log.txt")
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

    @enforce_snake_case
    @log_calls("./log.txt")
    def find_hotels_with_rating_greater_than(self, rating):
        """
        Find hotels with a rating greater than the specified value.

        Args:
            rating: A float representing the minimum rating.

        Returns:
            A list of hotel names that have a rating greater than the specified value.
        """
        return [hotel.name for hotel in self.hotels if hotel.rating > rating]

    def __len__(self):
        return len(self.hotels)

    def __getitem__(self, index):
        return self.hotels[index]

    def __iter__(self):
        return iter(self.hotels)

    @enforce_snake_case
    @log_calls("./log.txt")
    def get_all_locations(self):
        """
        Returns a list of locations for all hotels in the hotels list.

        Returns:
        list: A list of locations for all hotels in the hotels list.
        """
        return [hotel.get_location() for hotel in self.hotels]

    @enforce_snake_case
    @log_calls("./log.txt")
    def get_enumerated_hotels(self):
        """
        Prints an enumerated list of hotels in the hotels list.

        Returns:
        Output of zip (index_number, hotel_object)
        """
        for hotel in list(enumerate(self.hotels)):
            print(f"{hotel}")

    @enforce_snake_case
    @log_calls("./log.txt")
    def get_zip_locations(self):
        """
        Get zipped list of hotels with the result of the get_all_locations method.

        Returns:
            A list of tuples where each tuple contains the hotel
             object and the result of the get_all_locations method.
        """
        for hotel in list(zip(self.hotels, self.get_all_locations())):
            print(f"{hotel}")

    @enforce_snake_case
    @log_calls("./log.txt")
    def get_hotel_attributes_by_type(self, data_type):
        """
        Prints a dictionary containing attributes and
        their values for each hotel in the hotels list where
        attribute value type matches data_type.

        Args:
        data_type (type): The type to match attribute values against.

        Returns:
        None
        """
        for hotel in self.hotels:
            # pylint: disable = unidiomatic-typecheck
            hotel_attributes = {key: value for key, value in hotel.__dict__.items()
                                if type(value) == data_type}
            print(hotel_attributes)

    @enforce_snake_case
    @log_calls("./log.txt")
    def check_all_any_of_hotels(self, condition):
        """
        Checks if all or any of the hotels in the hotels list meet a specified condition.

        Args:
        condition (function): A function that takes a Hotel object as
        input and returns a boolean value.

        Returns:
        dict: A dictionary containing two keys - "all" and "any" - with
        boolean values indicating if all or any of the hotels meet
        the specified condition respectively.
        """
        all_result = all(condition(hotel) for hotel in self.hotels)
        any_result = any(condition(hotel) for hotel in self.hotels)
        return {"all": all_result, "any": any_result}

    @enforce_snake_case
    def MyMethod(self):
        print("MyMethod called")

    @log_calls("./log.txt")
    def my_method(self):
        print("my_method called")


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

    print("\nLength of list: ")
    # pylint: disable = unnecessary-dunder-call
    print(manager.__len__())

    print("\nGet second element of list: ")
    # pylint: disable = unnecessary-dunder-call
    print(manager.__getitem__(2))

    print("\nGet all locations of list: ")
    print(manager.get_all_locations())

    print("\nGet enumerated list of hotels: ")
    manager.get_enumerated_hotels()

    print("\nZipped list of hotels with locations:")
    manager.get_zip_locations()

    print("\nAttributes of hotels with int values:")
    manager.get_hotel_attributes_by_type(int)
    print()
    manager.get_hotel_attributes_by_type(str)

    print("\nUsing of all() and any():")
    print(manager.check_all_any_of_hotels(lambda hotel: hotel.available_rooms < 30))

    manager = HotelManager()
    manager.my_method()
    manager.MyMethod()


if __name__ == "__main__":
    main()
