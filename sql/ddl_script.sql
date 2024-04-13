CREATE TABLE Members (
    member_id SERIAL PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    date_of_birth DATE NOT NULL,
	enrollment_date DATE NOT NULL,
	member_role VARCHAR(1) NOT NULL CHECK (member_role IN ('t', 'm', 'a'))
);

CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,
    member_id INTEGER UNIQUE REFERENCES Members(member_id) NOT NULL
);

CREATE TABLE Admins (
    admin_id SERIAL PRIMARY KEY,
    member_id INTEGER UNIQUE REFERENCES Members(member_id) NOT NULL
);

CREATE TABLE FitnessGoals (
    goal_id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(member_id) NOT NULL,
    target_date DATE NOT NULL,
    target_value DECIMAL NOT NULL
);

CREATE TABLE HealthMetrics (
    metric_id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(member_id) NOT NULL,
    measurement_date DATE NOT NULL,
    body_weight DECIMAL NOT NULL,
    body_fat DECIMAL NOT NULL,
    muscle_mass DECIMAL NOT NULL,
    blood_pressure INTEGER NOT NULL
);

CREATE TABLE ExerciseRoutines (
    routine_id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(member_id) NOT NULL,
    routine_name VARCHAR(100) NOT NULL,
    routine_description TEXT NOT NULL
);

CREATE TABLE FitnessAchievements (
    achievement_id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(member_id) NOT NULL,
    achievement_desc TEXT NOT NULL,
    achievement_date DATE NOT NULL
);

CREATE TABLE TrainingSessions (
    session_id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(member_id) NOT NULL,
    trainer_id INTEGER REFERENCES Trainers(trainer_id) NOT NULL,
    week_day VARCHAR (3) NOT NULL CHECK (week_day IN ('mon','tue','wed','thu','fri','sat','sun')),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE TrainerAvailability (
    avail_id SERIAL PRIMARY KEY,
    trainer_id INTEGER REFERENCES Trainers(trainer_id) NOT NULL,
    week_day VARCHAR (3) NOT NULL CHECK (week_day IN ('mon','tue','wed','thu','fri','sat','sun')),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    avail VARCHAR(1) NOT NULL DEFAULT 'f' CHECK (avail IN ('f', 'b'))
);

CREATE TABLE Rooms (
    room_id SERIAL PRIMARY KEY,
    room_number VARCHAR(20) UNIQUE NOT NULL,
    capacity INTEGER NOT NULL
);

CREATE TABLE RoomBookings (
    booking_id SERIAL PRIMARY KEY,
    room_id INTEGER REFERENCES Rooms(room_id) NOT NULL,
    admin_id INTEGER REFERENCES Admins(admin_id) NOT NULL,
    week_day VARCHAR (3) NOT NULL CHECK (week_day IN ('mon','tue','wed','thu','fri','sat','sun')),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE GroupClasses (
    class_id SERIAL PRIMARY KEY,
    trainer_id INTEGER REFERENCES Trainers(trainer_id) NOT NULL,
    week_day VARCHAR (3) NOT NULL CHECK (week_day IN ('mon','tue','wed','thu','fri','sat','sun')),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL
);

CREATE TABLE Registrations (
    reg_id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(member_id) NOT NULL,
    class_id INTEGER REFERENCES GroupClasses(class_id) NOT NULL
);

CREATE TABLE Equipment (
    equipment_id SERIAL PRIMARY KEY,
    equip_name VARCHAR(100) NOT NULL,
    equip_status VARCHAR(1) NOT NULL DEFAULT 'b' CHECK (equip_status IN ('g', 'b'))
);

CREATE TABLE EquipmentMaintenance (
    maintenance_id SERIAL PRIMARY KEY,
    equipment_id INTEGER REFERENCES Equipment(equipment_id) NOT NULL,
    admin_id INTEGER REFERENCES Admins(admin_id) NOT NULL,
    maintenance_date DATE NOT NULL
);

CREATE TABLE Bills (
    bill_id SERIAL PRIMARY KEY,
    member_id INTEGER REFERENCES Members(member_id) NOT NULL,
    admin_id INTEGER REFERENCES Admins(admin_id) DEFAULT NULL,
    amount DECIMAL NOT NULL,
    bill_status VARCHAR(1) NOT NULL DEFAULT 'u' CHECK (bill_status IN ('u', 'p'))
);
