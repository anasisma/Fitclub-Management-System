from datetime import datetime

# function to check if date input is valid
def valid_date(date):
    try: # try creating a date object with the year, month, and date supplied
        year, month, day = map(int, date.split('-'))
        datetime(year=year, month=month, day=day)
        return True
    except ValueError: # if the object wasn't created, then the values were not valid
        return False
    
# Function to get all availabilities of logged in trainer
def viewAvailabilities(userId, conn):
    try:
        cur = conn.cursor()
        cur2 = conn.cursor()
        
        cur.execute(f"SELECT * FROM Trainers WHERE member_id = {userId}")
        trainer = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement

        # get the rows using the cursor
        cur2.execute(f"SELECT * FROM TrainerAvailability WHERE trainer_id = {trainer[0]}")
        # make a list of rows from the cursor
        rows = cur2.fetchall()
        
        cur.close()
        cur2.close()
        
        if (rows):
            print("Your availabilities are:")
            # print all the rows
            for row in rows:
                print(f"{row[0]}: Weekday: {row[2]}, start time: {row[3]}, end time: {row[4]}, are you busy (b) or free (f): {row[5]}")
            return rows
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        cur2.close()
        cur.close()
        return None
    
# Function to add a new availability for logged in trainer
def addAvailability(userId, week_day, start_time, end_time, conn):
    try:
        if (week_day in ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']):
            cur = conn.cursor()
            cur2 = conn.cursor()
            
            cur.execute(f"SELECT * FROM Trainers WHERE member_id = {userId}")
            trainer = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement
            
            # Insert new row into table
            cur2.execute(f""" 
                INSERT INTO TrainerAvailability (trainer_id, week_day, start_time, end_time) 
                VALUES ('{trainer[0]}', '{week_day}', '{start_time}', '{end_time}') """)
            
            cur.close()
            cur2.close()
            return True
        else:
            print("Please type the week day only using the first 3 letters. (i.e. mon, tue, ...)")
        
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        cur2.close()
        return False

# Function to search based on name
def profileSearch(name, conn):
    # get the rows using the cursor
    cur = conn.cursor()
    
    cur.execute(f"SELECT * FROM Members WHERE first_name ILIKE '%{name}%' OR last_name ILIKE '%{name}%';")

    # make a list of rows from the cursor
    rows = cur.fetchall()
    
    if (rows):
        # print all the rows
        for row in rows:
            print(f"Member ID: {row[0]}, name: {row[1]} {row[2]}, email address: {row[3]}")
    else:
        print("No members found.")