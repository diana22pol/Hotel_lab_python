from models.hotel import Hotel


class MountainHotel(Hotel):
    def __init__(self, name, total_rooms, available_rooms, rating, ski_lodge):
        super().__init__(name, total_rooms, available_rooms, rating)
        self.ski_lodge = ski_lodge

    def get_Location(self):
        return None

    def __str__(self):
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Ski Lodge: {self.ski_lodge}"
