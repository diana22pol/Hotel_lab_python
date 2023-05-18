from models.hotel import Hotel


class Motel(Hotel):
    def __init__(self, name, total_rooms, available_rooms, rating, track_number_nearby, track_kilometers, cities_nodes):
        super().__init__(name, total_rooms, available_rooms, rating)
        self.track_number_nearby = track_number_nearby
        self.track_kilometers = track_kilometers
        self.cities_nodes = cities_nodes

    def get_Location(self):
        return self.cities_nodes + "\t" + self.track_kilometers

    def __str__(self):
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Track Number Nearby: {self.track_number_nearby}, Track Kilometers: {self.track_kilometers}, " \
               f"Cities Nodes: {self.cities_nodes}"