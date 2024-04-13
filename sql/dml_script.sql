INSERT INTO Members (first_name, last_name, email, password, date_of_birth, enrollment_date, member_role)
VALUES ('First', 'Memb', 'first@email.com', 'p1', '1990-05-15', '2024-04-01', 'm'),
    ('Second', 'Membe', 'second@email.com', 'p2', '1985-08-21', '2024-04-02', 'm'),
    ('Third', 'Member', 'third@email.com', 'p3', '1995-03-10', '2024-04-03', 'm'),
    ('Fourth', 'Train', 'fourth@email.com', 'p4', '1982-11-30', '2024-04-04', 't'),
    ('Fifth', 'Trainer', 'fifth@email.com', 'p5', '1993-07-25', '2024-04-05', 't'),
    ('Sixth', 'Admin', 'sixth@email.com', 'p6', '1978-12-20', '2024-04-06', 'a');


INSERT INTO Trainers (member_id) VALUES (4), (5);
INSERT INTO Admins (member_id) VALUES (6);

INSERT INTO FitnessGoals (member_id, target_date, target_value)
VALUES (1, '2024-06-30', 70.5), (2, '2024-07-15', 65.0), (3, '2024-08-01', 60.0);

INSERT INTO HealthMetrics (member_id, measurement_date, body_weight, body_fat, muscle_mass, blood_pressure)
VALUES (1, '2022-04-12', 75.5, 18.0, 65.0, 120), (2, '2023-04-12', 68.0, 22.5, 60.0, 118), (3, '2024-04-12', 63.0, 20.0, 55.0, 122);

INSERT INTO ExerciseRoutines (member_id, routine_name, routine_description)
VALUES (1, 'Cardio', 'A cardio workout focusing on endurance.'),
    (2, 'Strength Training', 'A full-body strength training routine using free weights and machines.'),
    (3, 'Yoga', 'A yoga routine to improve flexibility and reduce stress.');
	
INSERT INTO FitnessAchievements (member_id, achievement_desc, achievement_date)
VALUES (1, 'Completed a 5K run in under 30 minutes.', '2024-04-10'),
    (2, 'New deadlift PR: 100kg.', '2024-04-11'),
    (3, 'Consistently practiced yoga for 30 days straight.', '2024-04-12');
	
INSERT INTO TrainingSessions (member_id, trainer_id, week_day, start_time, end_time)
VALUES (1, 1, 'mon', '09:00', '10:00'),
    (2, 2, 'wed', '10:00', '11:00'),
    (3, 1, 'fri', '11:00', '12:00');


INSERT INTO TrainerAvailability (trainer_id, week_day, start_time, end_time, avail)
VALUES (1, 'mon', '09:00', '10:00', 'b'),
	(1, 'tue', '10:00', '11:00', 'b'),
    (1, 'fri', '11:00', '12:00', 'b'),
	(1, 'sat', '09:00', '10:00', 'b'),
	(2, 'tue', '16:00', '17:00', 'f'),
	(2, 'wed', '10:00', '11:00', 'b'),
	(2, 'thu', '11:00', '12:00', 'b'),
	(2, 'fri', '11:00', '12:00', 'f');

INSERT INTO Rooms (room_number, capacity)
VALUES (101, 20),
    (102, 15),
    (103, 25);

INSERT INTO RoomBookings (room_id, admin_id, week_day, start_time, end_time)
VALUES (1, 1, 'mon', '09:00:00', '11:00:00');

INSERT INTO GroupClasses (trainer_id, week_day, start_time, end_time)
VALUES (1, 'tue', '10:00', '11:00'),
    (2, 'thu', '11:00', '12:00'),
    (1, 'sat', '09:00', '10:00');

INSERT INTO Registrations (member_id, class_id)
VALUES (1, 1),
    (2, 2),
    (3, 3);

INSERT INTO Equipment (equip_name, equip_status)
VALUES ('Treadmill', 'g'),
    ('Barbell', 'b'),
    ('Yoga Mat', 'g');

INSERT INTO EquipmentMaintenance (equipment_id, admin_id, maintenance_date)
VALUES (1, 1, '2024-04-10'),
    (3, 1, '2024-04-12');

INSERT INTO Bills (member_id, admin_id, amount, bill_status)
VALUES (1, NULL, 50.00, 'u'),
    (2, NULL, 60.00, 'u'),
    (3, NULL, 55.00, 'u');

