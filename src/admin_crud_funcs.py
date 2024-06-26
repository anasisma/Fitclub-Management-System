from datetime import datetime

def getAdminId(userId, conn):
    try:
        cur = conn.cursor()
        # get the row using the cursor
        cur.execute(f"SELECT * FROM Admins WHERE member_id = {userId}")
        row = cur.fetchone()
        
        if (row):
            return row[0]
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None
    
# Function to print all existing room bookings
def viewBookings(conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM RoomBookings")
        # make a list of rows from the cursor
        bookings = cur.fetchall()

        if (bookings):
            for row in bookings:
                # get the respective room from the Rooms table, to access the room number
                cur.execute(f"SELECT * FROM Rooms WHERE room_id = {row[1]}")
                room = cur.fetchone()
                
                print(f"Booking ID: {row[0]}, Room {room[1]}: capacity: {room[2]}, booked on {row[3]} between {row[4]} and {row[5]}")
                
            return bookings
        cur.close()
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None

# function to print all existing rooms
def viewRooms(conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM Rooms")
        # make a list of rows from the cursor
        rooms = cur.fetchall()

        for room in rooms:
            # print all the rooms' info
            print(f"Room ID: {room[0]}, Room {room[1]}: capacity: {room[2]}")
        cur.close()
    except Exception as e:
        print(f"Error: {e}")
        cur.close()

# function creates a new booking
def createBooking(room_id, userId, week_day, start_time, end_time, conn):
    try:
        
        admin_id = getAdminId(userId, conn)
        
        # execute the INSERT statement using the cursor
        cur = conn.cursor()
        cur.execute(f""" 
            INSERT INTO RoomBookings (room_id, admin_id, week_day, start_time, end_time) 
            VALUES ('{room_id}', '{admin_id}', '{week_day}', '{start_time}', '{end_time}') """)

        cur.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False

# function deletes a room booking
def deleteBooking(booking_id, conn):
    try:
        cur = conn.cursor()

        # check if a goal with the given id exists
        cur.execute(f"SELECT * FROM RoomBookings WHERE booking_id = {booking_id}")
        booking = cur.fetchone() # only fetch one row since the id is unique, which means there can only ever be one result to the select statement

        # execute and commit the DELETE statement
        if booking:
            cur.execute(f"""DELETE FROM RoomBookings WHERE booking_id = {booking_id}""")
            return True
        else:
            # if the function reaches this, then there was no row in the select statement
            print("Please enter a valid room booking id.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return False

# function displays all equipment and their maintenance state
def viewEquipment(conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM Equipment")
        # make a list of rows from the cursor
        equip = cur.fetchall()

        if (equip):
            for row in equip:
                
                # based on the value of equip_status, the equipment is in good state or bad
                state = row[2]
                if (state == 'b'):
                    state = 'Bad condition'
                elif (state == 'g'):
                    state = 'Good condition'
                
                print(f"{row[1]}, state: {state}")
                
            return equip
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None
    
# function displays all equipment in bad condition
def viewBadEquip(conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM Equipment WHERE equip_status = 'b'")
        # make a list of rows from the cursor
        equip = cur.fetchall()

        if (equip):
            print("The equipment currently needing maintenance are: ")
            for row in equip:
                print(f"ID: {row[0]}, {row[1]}")
                
            return equip
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None
    
# function maintains equipment with specified equipment id
def maintainEquip(equip_id, userId, maintenance_date, conn):
    admin_id = getAdminId(userId, conn)
    try:
        cur = conn.cursor()

        # add new entry into the "maintenance log"
        cur.execute(f"""
                    INSERT INTO EquipmentMaintenance (equipment_id, admin_id, maintenance_date)
                    VALUES ('{equip_id}', '{admin_id}', '{maintenance_date}')""")
        # change equipment's maintenance status to good condition
        cur.execute(f"UPDATE Equipment SET equip_status = 'g' WHERE equipment_id = {equip_id}")
        cur.close()
        return True
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
            print("The group fitness classes are: ")
            # print all the rows
            for row in rows:
                print(f"{row[0]}: Weekday: {row[2]}, start time: {row[3]}, end time: {row[4]}")
            return rows
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None

# function to modify specified attribute of a class
def modifyClass(class_id, change, new_value, conn):
    try:
        cur = conn.cursor()

        # set the new value using the cursor
        cur.execute(f"UPDATE GroupClasses SET {change} = '{new_value}' WHERE class_id = {class_id}")
        print("The class has been updated.")
        cur.close()
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None
    
# Function to get all bills
def viewBills(conn):
    try:
        cur = conn.cursor()

        # get the rows using the cursor
        cur.execute(f"SELECT * FROM Bills")
        # make a list of rows from the cursor
        rows = cur.fetchall()
        cur.close()
        
        if (rows):
            print("Here is the bill history of the fitness club: ")
            # print all the rows
            for row in rows:
                
                # based on the value of bill_status, the bill is paid or unpaid
                state = row[4]
                if (state == 'u'):
                    state = 'Unpaid'
                elif (state == 'p'):
                    state = 'Paid'
                
                print(f"Bill {row[0]}: Charged to member id: {row[1]}, amount: {row[3]}, status: {state}")
            return rows
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None

# Function to change payment status of specified bill
def handleBill(user_input, status, userId, conn):
    adminId = getAdminId(userId, conn)
    try:
        cur = conn.cursor()
        cur.execute(f"""UPDATE Bills SET bill_status = '{status}', admin_id = '{adminId}' WHERE bill_id = '{user_input}'""")
    except Exception as e:
        print(f"Error: {e}")
        cur.close()
        return None