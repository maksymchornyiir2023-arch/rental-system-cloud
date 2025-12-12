
-- Заповнення Users
INSERT INTO Users (username,email,phone) VALUES
('ivan123','ivan@example.com','+380631234567'),
('petro_p','petro@example.com','+380501112233'),
('olena_o','olena@example.com','+380671234890'),
('maria14','maria@example.com','+380991112345'),
('oleg71','oleg@example.com','+380631234568'),
('dima_k','dima@example.com','+380932221234'),
('alina_z','alina@example.com','+380972345678'),
('sergiy_b','sergiy@example.com','+380662345678'),
('vitaliy_d','vitaliy@example.com','+380502345678'),
('natalia_r','natalia@example.com','+380682345678');

-- UsersRoles
INSERT INTO UsersRoles (user_id,role) VALUES
(1,'customer'),(2,'customer'),(3,'customer'),(4,'admin'),(5,'customer'),
(6,'customer'),(7,'customer'),(8,'customer'),(9,'customer'),(10,'admin');

-- Locations
INSERT INTO Locations (name,address,capacity) VALUES
('Central Parking','вул. Головна, 1, Львів',50),
('Airport Parking','Рясне-2, Львів',100),
('Train Station','вул. Чернівецька, Львів',70),
('Forum Mall','вул. Під Дубом, 7, Львів',40),
('King Cross','вул. Стрийська, 30, Львів',90);

-- CarModels
INSERT INTO CarModels (manufacturer,model_name,engine) VALUES
('Toyota','Corolla','1.6L I4'),
('BMW','X3','2.0L I6'),
('Volkswagen','Golf','1.4L I4'),
('Renault','Kangoo','1.5L I4'),
('Mercedes','C-Class','2.0L I4');

-- Cars
INSERT INTO Cars (model_id,license_plate,current_status,current_location_id) VALUES
(1,'AE1234CT','available',1),
(2,'BC2345LV','available',1),
(3,'AB3456LT','maintenance',2),
(4,'CE4567LB','available',3),
(5,'DE5678LS','rented',2),
(1,'AA1111AA','available',4),
(2,'BB2222BB','available',5),
(3,'CC3333CC','rented',1),
(4,'DD4444DD','maintenance',3),
(5,'EE5555EE','available',4);

-- CarStatusHistory
INSERT INTO CarStatusHistory (car_id,status) VALUES
(1,'available'),(2,'available'),(3,'maintenance'),(4,'available'),(5,'rented'),
(6,'available'),(7,'available'),(8,'rented'),(9,'maintenance'),(10,'available');

-- CarLocationHistory
INSERT INTO CarLocationHistory (car_id,location_id) VALUES
(1,1),(2,1),(3,2),(4,3),(5,2),(6,4),(7,5),(8,1),(9,3),(10,4);

-- Rentals
INSERT INTO Rentals (user_id,car_id,location_id,start_date,end_date) VALUES
(1,5,2,'2025-06-10','2025-06-15'),
(2,1,1,'2025-06-12','2025-06-18'),
(3,2,1,'2025-06-05','2025-06-10'),
(5,4,3,'2025-06-14','2025-06-20'),
(1,3,2,'2025-06-20','2025-06-25'),
(6,6,4,'2025-06-01','2025-06-05'),
(7,7,5,'2025-06-03','2025-06-08'),
(8,8,1,'2025-06-06','2025-06-12'),
(9,9,3,'2025-06-09','2025-06-14'),
(10,10,4,'2025-06-11','2025-06-16');

-- Payments
INSERT INTO Payments (rental_id,amount,paid_at) VALUES
(1,250.00,'2025-06-10 09:00:00'),
(2,300.00,'2025-06-12 10:30:00'),
(3,150.00,'2025-06-05 08:45:00'),
(4,200.00,'2025-06-14 11:00:00'),
(5,275.00,'2025-06-20 14:15:00'),
(6,190.00,'2025-06-01 09:10:00'),
(7,210.00,'2025-06-03 10:00:00'),
(8,260.00,'2025-06-06 11:00:00'),
(9,280.00,'2025-06-09 12:00:00'),
(10,230.00,'2025-06-11 13:00:00');

-- Fines
INSERT INTO Fines (user_id,rental_id,amount,issued_at,description) VALUES
(1,1,50.00,'2025-06-12','Speeding'),
(2,2,30.00,'2025-06-14','Parking violation'),
(3,3,20.00,'2025-06-07','Red light'),
(5,4,40.00,'2025-06-15','Seatbelt'),
(1,5,60.00,'2025-06-22','Mobile use while driving'),
(6,6,35.00,'2025-06-03','Speeding'),
(7,7,25.00,'2025-06-05','Improper lane usage'),
(8,8,45.00,'2025-06-09','No lights'),
(9,9,30.00,'2025-06-11','Expired license'),
(10,10,55.00,'2025-06-13','Illegal U-turn');
