class Hotel:
    def __init__(self):
        self.available_rooms = []
        self.interesting_rooms = []

    def show_available(self):
        pass


class HotelRoom:
    def __init__(self, room_type, cost, number):
        self.room_type = room_type
        self.cost = cost
        self.number = number


class Terminal:
    hotel = Hotel()
