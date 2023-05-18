from models.beach_hotel import BeachHotel
from models.motel import Motel
from models.mountain_hotel import MountainHotel
from models.resort_hotel import ResortHotel


class HotelManager:
    @staticmethod
    def find_hotels_with_total_rooms_greater_than(total_rooms, hotel_list):
        return [hotel.name for hotel in filter(lambda hotel: hotel.total_rooms > total_rooms, hotel_list)]

    @staticmethod
    def find_hotels_with_rating_greater_than(rating, hotel_list):
        return [hotel.name for hotel in filter(lambda hotel: hotel.rating > rating, hotel_list)]

    @staticmethod
    def main():
        hotel_list = [Motel("Highway Motel", 30, 25, 3, "M4", "280 km", "Kyiv-Lviv"),
                      Motel("Highway Motel", 50, 25, 3, "M4", "280 km", "Kyiv-Lviv"),
                      ResortHotel("Beach Resort", 300, 150, 4, 2, 1, 7),
                      ResortHotel("Grand Resort", 500, 200, 5, 3, 2, 10),
                      BeachHotel("Marriott", 150, 62, 4, True),
                      BeachHotel("Hilton", 80, 22, 3, False),
                      MountainHotel("Winter holidays", 488, 70, 5, True),
                      MountainHotel("Ice Crystal Ski Resort", 656, 14, 5, True)]

        for hotel in hotel_list:
            print(str(hotel))

        print("\nHotels with total rooms greater than 200:")
        print(HotelManager.find_hotels_with_total_rooms_greater_than(200, hotel_list))
        print("\nHotels with rating greater than 4:")
        print(HotelManager.find_hotels_with_rating_greater_than(4, hotel_list))


HotelManager.main()
