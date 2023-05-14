class Hotel:
    """
    Represents a hotel with its name, number of total rooms, number of available rooms and rating.
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
        self._name = name
        self._total_rooms = total_rooms
        self._available_rooms = available_rooms
        self._rating = rating

    def book_room(self):
        """
        Books a room in the hotel.
        """
        if self._available_rooms > 0:
            self._available_rooms -= 1

    def release_room(self):
        """
        Releases a room in the hotel.
        """
        if self._available_rooms < self._total_rooms:
            self._available_rooms += 1

    def get_available_rooms(self):
        """
        Returns the number of available rooms in the hotel.
        """
        return self._available_rooms

    def get_booked_rooms_count(self):
        """
        Returns the number of booked rooms in the hotel.
        """
        return self._total_rooms - self._available_rooms

    @staticmethod
    def get_instance():
        """
        Returns a singleton instance of the Hotel class.
        """
        if not Hotel.__instance:
            Hotel.__instance = Hotel()
        return Hotel.__instance


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
