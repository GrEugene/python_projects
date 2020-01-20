from room import Room

class Manager:
    rooms = []

    def __init__(self):
        n1 = Room("N1", "Business", 1)
        n2 = Room("N2", "De luxe", 2)
        n3 = Room("N3", "President", 2)
        n4 = Room("N4", "Business", 1)
        self.rooms = [n1, n2, n3, n4]

    def show_hotel_menu(self):
        print('****** Hotel Mumbai *****\n')
        print('1. Show information for all rooms')
        print('2. Show only free rooms')
        print('3. Reserve room')
        print('4. Unreserve room')
        print('5. Quit\n')

    def option_1(self):
        for room in self.rooms:
            room.room_info()

    def option_2(self):
        for room in self.rooms:
            if room.is_reserve == False:
                room.room_info()

    def option_3(self):
        print('Input room number for reserving: ')
        number = str(input())
        for room in self.rooms:
            if number == room.number and room.is_reserve == False:
                room.is_reserve = True
                print('Room was reserved')
                break
            elif number == room.number and room.is_reserve == True:
                print('Room already reserved')
                break
            else:
                print('Room was not found')

    def option_4(self):
        print('Input room number for checking out: ')
        number = str(input())
        for room in self.rooms:
            if number == room.number and room.is_reserve == True:
                room.is_reserve = False
                print('Room was checked out')
                break
            elif number == room.number and room.is_reserve == False:
                print('Room already checked out')
                break
            else:
                print('Room was not found')
