from random import randint


def generate_rooms():
    rooms_attributes = [
        ('Бедный', 1000),
        ('Простой', 4000),
        ('Повышенной комфортности', 6500),
        ('Люкс', 14000),
        ('Супер люкс', 20000),
        ('Презедентский', 40000)
    ]

    for number in range(10):
        random_number = randint(0, 5)
        yield HotelRoom(rooms_attributes[random_number][0],
                        rooms_attributes[random_number][1],
                        number + 1)


class Hotel:
    def __init__(self):
        self.rooms = [*[room for room in generate_rooms()]]
        self.arend_rooms = []

    def show_available_rooms(self):
        for room in self.rooms:
            if room.state is True:
                yield room.__str__()

    def show_arend_rooms(self):
        if self.arend_rooms is False:
            return 'Нет арендованных домов'
        else:
            

    def arend_room(self, number):
        for room in self.rooms:
            if room.state is True and room.number == number:
                room.state = False
                self.arend_rooms.append(room)

    def arend_cost(self):
        cost = 0
        for room in self.arend_rooms:
            cost += room.cost

        return cost


class HotelRoom:
    def __init__(self, room_type, cost, number):
        self.room_type = room_type
        self.cost = cost
        self.number = number
        self.state = bool(randint(0, 1))

    def __str__(self):
        return f'Тип номера: {self.room_type}\n' \
               f'Цена: {self.cost}\n' \
               f'Номер: {self.number}'


class Terminal:
    def __init__(self):
        self.hotel = Hotel()

    def arend_room(self):
        print('Свободные номера:')
        for room in self.hotel.show_available_rooms():
            print(room.__str__(), '\n------')

        self.hotel.arend_room(randint(0, 9))

        print('арендованные номера:')


def main():
    terminal = Terminal()
    terminal.arend_room()


if __name__ == '__main__':
    main()
