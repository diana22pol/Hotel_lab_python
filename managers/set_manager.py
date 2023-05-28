"""
Importing of classes for set manager
"""
# pylint: disable = import-error
from models.beach_hotel import BeachHotel
from models.motel import Motel
from models.mountain_hotel import MountainHotel
from models.resort_hotel import ResortHotel
from managers.hotel_manager import HotelManager


class SetManager:
    def __init__(self, hotel_manager):
        self.hotels = hotel_manager
        self.index = 0
        self.set_data = []
        for plate in self.hotels:
            for working_day in plate:
                self.set_data.append(working_day)

    def __iter__(self):
        return self

    def __getitem__(self, index):
        return self.set_data[index]

    def __next__(self):
        if self.index >= len(self):
            raise StopIteration
        result = self.set_data[self.index]
        self.index += 1
        return result

    def __len__(self):
        return len(self.set_data)


def main():
    manager = HotelManager()

    manager.add_hotel(Motel("Highway Motel", 30, 25, 3, "M4", "280 km", "Kyiv-Lviv"))
    manager.add_hotel(Motel("Highway Motel", 50, 25, 3, "M4", "280 km", "Kyiv-Lviv"))
    manager.add_hotel(ResortHotel("Beach Resort", 300, 150, 4, 2, 1, 7))
    manager.add_hotel(ResortHotel("Grand Resort", 500, 200, 5, 3, 2, 10))
    manager.add_hotel(BeachHotel("Marriott", 150, 62, 4, True))
    manager.add_hotel(BeachHotel("Hilton", 80, 22, 3, False))
    manager.add_hotel(MountainHotel("Winter holidays", 488, 70, 5, True))
    manager.add_hotel(MountainHotel("Ice Crystal Ski Resort", 656, 14, 5, True))

    set_manager = SetManager(manager)


    print("The length of the new list:")
    print(len(set_manager))
    print()
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))
    print(next(set_manager))

    for work_day in set_manager:
        print(work_day)


if __name__ == "__main__":
    main()
