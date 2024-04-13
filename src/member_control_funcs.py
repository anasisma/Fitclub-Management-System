from member_crud_funcs import *

# Function for control sequence of profile management
def profileManagement(currSession, conn):
    while True:
        print()
        print("Welcome to profile management. Here are your options:")
        print("1: Viewing personal information.")
        print("2: Updating personal information.")
        print("3: Managing fitness goals.")
        print("4: Managing health metrics.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            viewUserInfo(currSession[0], conn)
        
        elif user_input == '2':
        
            field = input("Please enter the field you want to modify: ")
            new_value = input("Please enter the new value: ")
            updateProfile(currSession[0], field, new_value, conn)
            
        elif user_input == '3':
            fitnessManagement(currSession, conn)
            
        elif user_input == '4':
            metricsManagement(currSession, conn)
        
        elif user_input == 'b':
            break
        
        else:
            print("Please enter a valid selection.")
        
def addMemberC(conn):   
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    date_of_birth = input("Please enter your birth date (format is YYYY-MM-DD): ")
    enrollment_date = datetime.today().strftime('%Y-%m-%d')
    
    if(addMember(first_name, last_name, email, password, date_of_birth, enrollment_date, conn)):
        print(f"Congrats {first_name}, you are now registered to the fitness club!")
        
        
def fitnessManagement(currSession, conn):
    while True:
        print()
        print("Welcome to fitness goal management. Here are your options:")
        print("1: Viewing current fitness goal.")
        print("2: Adding a fitness goal.")
        print("4: Deleting a fitness goal.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            viewFitnessGoal(currSession[0], conn)
        
        elif user_input == '2':
            date = input("Please enter your target date (format is YYYY-MM-DD): ")
            goal = input("Please enter the weight goal: ")
            if(addFitnessGoal(currSession[0], date, goal, conn)):
                print("Fitness goal added successfully!")
                
        elif user_input == '4':
            if (deleteFitnessGoal(currSession[0], conn)):
                print("Your oldest fitness goal has been successfully deleted.")
        
        elif user_input == 'b':
            break
        else:
            print("Please enter a valid selection.")     
        
        
def metricsManagement(currSession, conn):
    while True:
        print()
        print("Welcome to health metrics management. Here are your options:")
        print("1: Viewing your health metrics over time.")
        print("2: Measuring your metrics.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            viewMetrics(currSession[0], conn)
        
        elif user_input == '2':
            if(measureMetrics(currSession[0], conn)):
                print("Metrics measured successfully!")
        
        elif user_input == 'b':
            break
        else:
            print("Please enter a valid selection.")     
            
def dashboard(currSession, conn):
    while True:
        print()
        print("Welcome to your dashboard. Here are your options:")
        print("1: Viewing your exercise routines.")
        print("2: Managing your fitness achievements.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            viewRoutines(currSession[0], conn)
        
        elif user_input == '2':
            achievementManagement(currSession, conn)
        
        elif user_input == 'b':
            break
        else:
            print("Please enter a valid selection.")     
        
def achievementManagement(currSession, conn):
    while True:
        print()
        print("Welcome to achievements management. Here are your options:")
        print("1: Viewing your fitness achievements.")
        print("2: Adding a new achievement.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            viewAchievements(currSession[0], conn)
        
        elif user_input == '2':
            date = input("Please enter the date of the achievement (format is YYYY-MM-DD): ")
            ach = input("Please enter a description of the achievement: ")
            if(addAchievement(currSession[0], date, ach, conn)):
                print("Achievement added successfully!")
        
        elif user_input == 'b':
            break
        else:
            print("Please enter a valid selection.")     
            
def memberScheduleManagement(currSession, conn):
    while True:
        print()
        print("Welcome to schedule management. Here are your options:")
        print("1: Sheduling a personal training session.")
        print("2: Viewing your booked personal training sessions.")
        print("3: Canceling a booked personal training session.")
        print("4: Joining a fitness class.")
        print("5: Viewing your fitness classes.")
        print("b: Go back to previous menu.")
        
        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            avails = viewAvailabilities(conn)
            if (avails):
                user_input = input("Please enter the availability you would like to request: ")
                if(selectAvailability(currSession[0],user_input,conn)):
                    print("You have succesfully booked your desired personal training session.")
                else:
                    print("Unable to book session.")
        
        elif user_input == '2':
            if not (viewBookedSessions(currSession[0], conn)):
                print("You have no sessions currently booked.")
                
        elif user_input == '3':
            if not (viewBookedSessions(currSession[0], conn)):
                print("You have no sessions currently booked.")
                
            user_input = input("Please enter the session you would like to cancel: ") 
            
            if (cancelSession(currSession[0], user_input, conn)):
                print("This session has been canceled.")
            else:
                print("Unable to cancel session.")
                
        elif user_input == "4":
            classes = viewClasses(conn)
            if (classes):
                user_input = input("Please enter the class you would like to join: ")
                if(joinClass(currSession[0],user_input,conn)):
                    print("You have succesfully been registered to this fitness class.")
                else:
                    print("Unable to cancel register to this fitness class.")   
                    
        elif user_input == '5':
            if not (viewJoinedClasses(currSession[0], conn)):
                print("You are registered in no fitness classes.")     
        
        elif user_input == 'b':
            break
        
        else:
            print("Please enter a valid selection.")