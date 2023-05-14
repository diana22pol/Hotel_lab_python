class Hotel:
    """
       Represents a hotel with its name, number of total rooms, number of available rooms and rating.
    """
    __instance = None

    def __init__(self, name="", totalRooms=None, availableRooms=None, rating=None):
        """
            Initializes a Hotel object.

            Parameters:
            name (str): The name of the hotel.
            total_rooms (int): The total number of rooms in the hotel.
            available_rooms (int): The number of available rooms in the hotel.
            rating (float): The rating of the hotel.

        """
        self._name = name
        self._totalRooms = totalRooms
        self._availableRooms = availableRooms
        self._rating = rating

    def bookRoom(self):
        """
            Books a room in the hotel.
        """
        if self._availableRooms > 0:
            self._availableRooms -= 1

    def releaseRoom(self):
        """
            Releases a room in the hotel.
        """
        if self._availableRooms < self._totalRooms:
            self._availableRooms += 1

    def getAvailableRooms(self):
        """
            Returns the number of available rooms in the hotel.
        """
        return self._availableRooms

    def getBookedRoomsCount(self):
        """
            Returns the number of booked rooms in the hotel.
        """
        return self._totalRooms - self._availableRooms

    @staticmethod
    def getInstance():
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
        Hotel.getInstance(),
        Hotel.getInstance()
    ]

    for hotel in hotels:
        print(
            f"Hotel: {hotel._name}, Total Rooms: {hotel._totalRooms}, Available Rooms: {hotel._availableRooms}, "
            f"Rating: {hotel._rating}")
