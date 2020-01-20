from manager import Manager

manager = Manager()
option = 0

while option != 5:
    manager.show_hotel_menu()
    option = print('Select option :')
    option = int(input())

    if option == 1:
        manager.show_all_rooms()
    elif option == 2:
        manager.show_all_free_rooms()
    elif option == 3:
        manager.reserve_room()
    elif option == 4:
        manager.unreserve_room()

