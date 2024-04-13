import psycopg2
from datetime import datetime
import random

# function to check if date input is valid
def valid_date(date):
    try: # try creating a date object with the year, month, and date supplied
        year, month, day = map(int, date.split('-'))
        datetime(year=year, month=month, day=day)
        return True
    except ValueError: # if the object wasn't created, then the values were not valid
        return False

def addMember(first_name, last_name, email, password, date_of_birth, enrollment_date, conn):
    try:
        # check if the date is valid
        if not valid_date(enrollment_date) or not valid_date(date_of_birth):
            print("Error: Please enter valid dates in the format YYYY-MM-DD.")
            return False

        # execute the INSERT statement using the cursor
        cur = conn.cursor()
        cur.execute(f""" 
            INSERT INTO Members (first_name, last_name, email, password, date_of_birth, enrollment_date, member_role) 
            VALUES ('{first_name}', '{last_name}', '{email}', '{password}', '{date_of_birth}', '{enrollment_date}', 'm') """)

        cur.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False

# Function to update profile
def updateProfile(member_id, field, new_value, conn):
    try:
        # Execute the UPDATE statement using the cursor
        cur = conn.cursor()
        cur.execute(f"UPDATE Members SET {field} = '{new_value}' WHERE member_id = {member_id}")
        print("Profile updated successfully.")
        cur.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False

# Function to view health metrics of logged in user
def viewMetrics(userId, conn):
    cur = conn.cursor()

    # get the rows using the cursor
    cur.execute(f"SELECT * FROM HealthMetrics WHERE member_id = {userId}")
    # make a list of rows from the cursor
    rows = cur.fetchall()

    print("Your previously recorded health metrics are:")
    # print all the rows
    for row in rows:
        print(f"Date: {row[2]}, weight: {row[3]}, body fat percentage: {row[4]}, muscle mass (kg): {row[5]}, blood pressure: {row[6]}")
        
def measureMetrics(userId, conn):
    try:
        # Get current date as date of measurement
        measure_date = datetime.today().strftime('%Y-%m-%d')
        # execute the INSERT statement using the cursor
        cur = conn.cursor()
        cur.execute(f""" 
            INSERT INTO HealthMetrics (member_id, measurement_date, body_weight, body_fat, muscle_mass, blood_pressure) 
            VALUES ('{userId}', '{measure_date}', '{round(random.uniform(45, 100), 1)}', '{round(random.uniform(5, 40) / 100, 1)}', '{round(random.uniform(30, 100), 1)}', '{round(random.randint(90, 140))}') """)

        cur.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False

# Function to view fitness goal of logged in user
def viewFitnessGoal(userId, conn):
    cur = conn.cursor()

    # check if a member with the given id exists
    cur.execute(f"SELECT * FROM FitnessGoals WHERE member_id = {userId}")
    goal = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement

    if goal:
            print("Your current fitness goal:")
            print("Target weight:", goal[3])
            print("Target date for this goal:", goal[2])
    else:
        print('There was an error retreiving your fitness goal.')

# Function to add a fitness goal for a member
def addFitnessGoal(userId, target_date, target_value, conn):
    try:
        # check if the date is valid
        if not valid_date(target_date):
            print("Error: Please enter valid dates in the format YYYY-MM-DD.")
            return False

        # execute the INSERT statement using the cursor
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO FitnessGoals (member_id, target_date, target_value) 
                       VALUES ('{userId}', '{target_date}', '{target_value}')""")

        cur.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False

# Function to update a fitness goal
def updateFitnessGoal(member_id, new_date, new_target, conn):
    try:
        # Execute the UPDATE statement using the cursor
        cur = conn.cursor()
        cur.execute(f"UPDATE FitnessGoals SET target_date = '{new_date}', target_value = '{new_target}' WHERE member_id = {member_id}")
        print("Fitness goal updated successfully.")
        cur.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False

# Function for deleting current user's fitness goal
def deleteFitnessGoal(member_id, conn):
    cur = conn.cursor()

    # check if a goal with the given id exists
    cur.execute(f"SELECT * FROM FitnessGoals WHERE member_id = {member_id}")
    goal = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement

    # execute and commit the DELETE statement
    if goal:
        cur.execute(f"""DELETE FROM FitnessGoals WHERE member_id = {member_id}""")
        return True
    
    # if the function reaches this, then there was no row in the select statement
    print("You did not have a fitness goal. Did you mean to create a new one?")
    return False

# Function to view current logged in user's personal information
def viewUserInfo(userId, conn):
    cur = conn.cursor()

    # get the rows using the cursor
    cur.execute(f"SELECT * FROM Members WHERE member_id = {userId}")
    existing_member = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement

    if existing_member:
            print("Personal Information:")
            print("First Name:", existing_member[1], ", Last Name:", existing_member[2])
            print("Email:", existing_member[3])
            print("Date of Birth:", existing_member[5])
            print("Enrollment Date:", existing_member[6])
    else:
        print('There was an error retreiving your personal information.')

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
    
# Function to view health metrics of logged in user
def viewRoutines(userId, conn):
    cur = conn.cursor()

    # get the rows using the cursor
    cur.execute(f"SELECT * FROM ExerciseRoutines WHERE member_id = {userId}")
    # make a list of rows from the cursor
    rows = cur.fetchall()

    print("Your workout routines are:")
    # print all the rows
    for row in rows:
        print(f"Name: {row[2]}, description: {row[3]}")

# Function to view fitness achievements of user  
def viewAchievements(userId, conn):
    cur = conn.cursor()

    # get the rows using the cursor
    cur.execute(f"SELECT * FROM FitnessAchievements WHERE member_id = {userId}")
    # make a list of rows from the cursor
    rows = cur.fetchall()

    print("Your fitness achievements are:")
    # print all the rows
    for row in rows:
        print(f"Date achieved: {row[3]}, achievement: {row[2]}")
        
# Function to add an achievement for a member
def addAchievement(userId, date, ach, conn):
    try:
        # check if the date is valid
        if not valid_date(date):
            print("Error: Please enter valid dates in the format YYYY-MM-DD.")
            return False

        # execute the INSERT statement using the cursor
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO FitnessAchievements (member_id, achievement_date, achievement_desc) 
                       VALUES ('{userId}', '{date}', '{ach}')""")

        cur.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False
    
# Function to get all 'free' availabilities
def viewAvailabilities(conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM TrainerAvailability WHERE avail = 'f'")
        # make a list of rows from the cursor
        rows = cur.fetchall()
        cur.close()
        if (rows):
            print("The open availabilities for personal sessions are:")
            # print all the rows
            for row in rows:
                print(f"{row[0]}: Weekday: {row[2]}, start time: {row[3]}, end time: {row[4]}")
            return rows
        else:
            print("Sorry, there are no open trainer availabilities.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None

# Function to book a trainer availability slot, which makes it become 'busy'
def selectAvailability(userId, avail_id, conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM TrainerAvailability WHERE avail = 'f' AND avail_id = {avail_id}")
        avail = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement
        
        if (avail):
            # make the trainer's availability become busy in the trainer's table
            cur.execute(f"UPDATE TrainerAvailability SET avail = 'b' WHERE avail_id = {avail_id}")
            # add this new session into the sessions table
            cur.execute(f""" INSERT INTO TrainingSessions (member_id, trainer_id, week_day, start_time, end_time) VALUES 
                ('{userId}', '{avail[1]}', '{avail[2]}', '{avail[3]}', '{avail[4]}') """)
            cur.close()
            return True
        else:
            cur.close()
            return False
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False
    
# Function to view Booked Sessions of user
def viewBookedSessions(userId, conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM TrainingSessions WHERE member_id = {userId}")
        # make a list of rows from the cursor
        rows = cur.fetchall()
        cur.close()

        print("Your booked sessions are:")
        # print all the rows
        for row in rows:
            print(f"{row[0]}: Weekday: {row[3]}, start time: {row[4]}, end time: {row[5]}")
        return rows
    
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None
    
# Function to cancel a personal training session
def cancelSession(userId, sess_id, conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM TrainingSessions WHERE member_id = {userId} AND session_id = {sess_id}")
        sess = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement
        
        if (sess):
            # remove this session from the sessions table
            cur.execute(f"DELETE FROM TrainingSessions WHERE session_id = {sess[0]}")
            # make the trainer's availability become free in the trainer's table
            cur.execute(f"UPDATE TrainerAvailability SET avail = 'f' WHERE trainer_id = {userId} AND start_time = '{sess[4]}'")
            cur.close()
            return True
        else:
            cur.close()
            return False
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False
    
# Function to get all open fitness classes
def viewClasses(conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM GroupClasses")
        # make a list of rows from the cursor
        rows = cur.fetchall()
        cur.close()
        if (rows):
            print("The open group fitness classes are: ")
            # print all the rows
            for row in rows:
                print(f"{row[0]}: Weekday: {row[2]}, start time: {row[3]}, end time: {row[4]}")
            return rows
        else:
            print("Sorry, there are no open group fitness classes.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None

# Function to book a trainer availability slot, which makes it become 'busy'
def joinClass(userId, class_id, conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM GroupClasses WHERE class_id = {class_id}")
        exists_class = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement
        
        if (exists_class):
            # add a new registration entry, to represent the member being in the class, into the registrations table
            cur.execute(f""" INSERT INTO Registrations (member_id, class_id) VALUES 
                ('{userId}', '{class_id}') """)
            cur.close()
            return True
        else:
            cur.close()
            return False
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False
    
# Function to view joined fitness classes of user
def viewJoinedClasses(userId, conn):
    try:
        cur = conn.cursor()
        cur2 = conn.cursor()
        
        # get the rows using the cursor
        cur.execute(f"SELECT * FROM Registrations WHERE member_id = {userId}")
        # make a list of rows from the cursor
        rows = cur.fetchall()
        cur.close()
        
        print("Your fitness classes are:")
        
        # list to contain all class id's that the user is registered in
        classes = []
        
        for row in rows:
            classes.append(row[2])

        for c in classes:
            # get the rows using the cursor
            cur2.execute(f"SELECT * FROM GroupClasses WHERE class_id = {c}")
            cl = cur2.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement
            print(f"{cl[0]}: Weekday: {cl[2]}, start time: {cl[3]}, end time: {cl[4]}")
            
        return rows
    
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None