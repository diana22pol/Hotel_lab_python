from models.hotel import Hotel


class ResortHotel(Hotel):
    def __init__(self, name, total_rooms, available_rooms, rating, child_pools, adult_pools, restaurants_number):
        super().__init__(name, total_rooms, available_rooms, rating)
        self.child_pools = child_pools
        self.adult_pools = adult_pools
        self.restaurants_number = restaurants_number

    def get_Location(self):
        return self.name

    # hotel_list.append(ResortHotel("Beach Resort", 300, 150, 4, 2, 1, 7))
    def __str__(self):
        return f"Hotel: {self.name}, Total Rooms: {self.total_rooms}, " \
               f"Available Rooms: {self.available_rooms}, Rating: {self.rating}, " \
               f"Child Pools: {self.child_pools}, Track Kilometers: {self.adult_pools}, " \
               f"Cities Nodes: {self.restaurants_number}"
