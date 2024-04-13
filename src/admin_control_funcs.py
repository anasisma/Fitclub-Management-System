from admin_crud_funcs import *
            
def roomManagement(currSession, conn):
    while True:
        print()
        print("Welcome to room booking management. Here are your options:")
        print("1: Viewing room bookings.")
        print("2: Creating new booking.")
        print("3: Deleting a booking.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            if not (viewBookings(conn)):
                print("There are no room bookings currently.")
        
        elif user_input == '2':
            # display all rooms so user knows what they can book
            viewRooms(conn)
            print()
            
            room_id = input("Please enter the ID of the room to book: ")
            week_day = input("Please enter day of the week: ")
            start_time = input("Please enter the start time: ")
            end_time = input("Please enter the end time: ")
    
            if(createBooking(room_id, currSession[0], week_day, start_time, end_time, conn)):
                print(f"The room has been successfully booked.")            
            
        elif user_input == '3':
            viewBookings(conn)
            print()
            
            booking_id = input("Please enter the ID of the room to book: ")
            
            if(deleteBooking(booking_id, conn)):
                print(f"The booking has been deleted.")  
        
        elif user_input == 'b':
            break
        
        else:
            print("Please enter a valid selection.")
            
def equip_maintenance(currSession, conn):
    while True:
        print()
        print("Welcome to equipment maintenance. Here are your options:")
        print("1: Viewing equipment.")
        print("2: Maintaining equipment.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            if not (viewEquipment(conn)):
                print("There is no equipment.")
        
        elif user_input == '2':
            # display all bad equipment so user knows what they can maintain
            if (viewBadEquip(conn)):
                print()
                
                equip_id = input("Please enter the ID of the equipment to maintain: ")
                # Get current date as date of measurement
                maintenance_date = datetime.today().strftime('%Y-%m-%d')
        
                if(maintainEquip(equip_id, currSession[0], maintenance_date, conn)):
                    print(f"The equipment has been restored.")
            else:
                print("All equipment is already in good state.")
        
        elif user_input == 'b':
            break
        
        else:
            print("Please enter a valid selection.")
            
def classManagement(conn):
    while True:
        print()
        print("Welcome to class schedule management. Here are your options:")
        print("1: Viewing class schedules.")
        print("2: Modifying an existing class.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            if not (viewClasses(conn)):
                print("There are no group fitness classes.")
        
        elif user_input == '2':
            if not (viewClasses(conn)):
                print("There are no group fitness classes.")
            else:
                user_input = input("Please enter the ID of the class to modify: ")
                change = input("Please enter what would you like to modify: ")
                new_value = input("Please enter the desired new value: ")
                modifyClass(user_input, change, new_value, conn)
        
        elif user_input == 'b':
            break
        
        else:
            print("Please enter a valid selection.")
            
def billManagement(curSession, conn):
    while True:
        print()
        print("Welcome to bill/payment management. Here are your options:")
        print("1: Viewing all bills.")
        print("2: Handling payment of a bill.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            if not (viewBills(conn)):
                print("There are no recorded bills.")
        
        elif user_input == '2':
            if not (viewBills(conn)):
                print("There are no recorded bills.")
            else:
                user_input = input("Please enter the ID of the bill to handle: ")
                status = input("Please enter the new status of the bill (u/p): ")
                handleBill(user_input, status, curSession[0], conn)
        
        elif user_input == 'b':
            break
        
        else:
            print("Please enter a valid selection.")