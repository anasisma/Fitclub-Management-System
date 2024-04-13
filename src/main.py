from member_control_funcs import *
from trainer_control_funcs import *

# values to modify to establish the connection
db = "FinalProj"
dbuser = "postgres"
dbpassword = "postgres"
dbhost = "localhost"
dbport = "5432"

# establish a connection to the db
conn = psycopg2.connect(database = db, user = dbuser, password = dbpassword, host = dbhost, port = dbport)
conn.autocommit = True

# Function to log in
def login(email, conn):
    try:
        # check if a member with the given email exists
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM Members WHERE email = '{email}'") 
        member = cur.fetchone() # only fetch one row since the email is unique, which means there can only ever be one result to the select statement
        
        # Make the user input the password, and if correct, then make the global session variable represent the currently logged in user
        if member:
            password = input("Please enter your password: ")
            if member[4] == password:
                cur.close()
                return member
            else:
                print("Incorrect password.")
                cur.close()
                return None
        
        else:
            # if the function reaches this, then there was no row in the select statement
            print("There is no member with this email. Did you mean to register?")
            cur.close()
            return None
        
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False

# Function to log out
def logout():
    # Clear the current session
    currSession = None

# Function to check if a user is logged in
def isLoggedIn(currSession):
    return currSession is not None

# Function to get the current session's role
def getRole(currSession):
    if currSession:
        return currSession[7]
    else:
        return None

# Global variable to store the current session
currSession = None

while True:

    # call a function based on the input of the user, or quit for input 'q'

    # the nested if statements are used for checking if the functions return true, which means that the execution went through properly
    # each function returns true or false based on a try-except block
    
    if not isLoggedIn(currSession):
        print()
        print("Options:")
        print("1: Register for the club.")
        print("2: Log into existing account.")
        print("q: Exit the program.")

        user_input = input("Please enter your selection: ")
        print()

        if user_input == "1":
            addMemberC(conn)
                
        elif user_input == "2":
            email = input("Please enter your email: ")
            currSession = login(email, conn)
            if(currSession is not None):
                print(f"{currSession[1]}, you are now logged in!")
                
        elif user_input == "q":
            break
        else:
            print("Please enter a valid selection.")
    
    elif isLoggedIn(currSession) and (getRole(currSession) == 'm'):
        print()
        print("Options:")
        print("1: Profile management.")
        print("2: Dashboard display.")
        print("3: Schedule management.")
        print("0: Log out of account.")
        print("q: Exit the program.")

        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            profileManagement(currSession, conn)
            
        elif user_input == "2":
            dashboard(currSession, conn)
            
        elif user_input == "3":
            scheduleManagement(currSession, conn)
            
        elif user_input == "0":
            currSession = logout()
                
        elif user_input == "q":
            break
        else:
            print("Please enter a valid selection.")

    elif isLoggedIn(currSession) and (getRole(currSession) == 't'):
        print()
        print("Options:")
        print("1: Schedule management.")
        print("2: Member profile viewing.")
        print("0: Log out of account.")
        print("q: Exit the program.")

        user_input = input("Please enter your selection: ")
        print()
        
        if user_input == "1":
            scheduleManagement(currSession, conn)
            
        elif user_input == "2":
            profileViewing(conn)
            
        elif user_input == "0":
            currSession = logout()
                
        elif user_input == "q":
            break
        
        else:
            print("Please enter a valid selection.")            
            