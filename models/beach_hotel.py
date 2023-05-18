from models.hotel import Hotel


class BeachHotel(Hotel):
    def __init__(self, name, total_rooms, available_rooms, rating, beach_front):
        super().__init__(name, total_rooms, available_rooms, rating)
        self.beach_front = beach_front;

    def get_Location(self):
        return None

    def __str__(self):
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Beach Front: {self.beach_front}"