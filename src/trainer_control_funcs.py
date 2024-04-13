from trainer_crud_funcs import *
            
def scheduleManagement(currSession, conn):
    while True:
        print()
        print("Welcome to schedule management. Here are your options:")
        print("1: Viewing your availabilities.")
        print("2: Adding a new availability slot.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            if not (viewAvailabilities(currSession[0], conn)):
                print("You currently have no availabilities.")
        
        elif user_input == '2':
            addAvail(currSession[0], conn)
        
        elif user_input == 'b':
            break
        
        else:
            print("Please enter a valid selection.")
            
def addAvail(userId, conn):   
    week_day = input("Please enter day of the week: ")
    start_time = input("Please enter the start time: ")
    end_time = input("Please enter the end time: ")
    
    if(addAvailability(userId, week_day, start_time, end_time, conn)):
        print(f"The timeslot has been successfully added.")
        
def profileViewing(conn):
    print()
    user_input = input("Please enter the name to search for: ")
    print()
    
    profileSearch(user_input, conn)