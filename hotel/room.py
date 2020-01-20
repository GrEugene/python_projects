class Room:
    number = ""
    category = ""
    floor = ""
    is_reserve = False

    def __init__(self, number, category, floor):
        self.number = number
        self.category = category
        self.floor = floor

    def room_info(self):
        print("Room number : ", self.number, ", category : ", self.category, ", floor : ", self.floor, ", is reserved : ", self.is_reserve)

    def reserve_room():
        self.is_reserve = True

    def unreserve_room():
        self.is_reserve = False
