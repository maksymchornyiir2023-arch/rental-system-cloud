USE maksim_rental;

-- Users
INSERT INTO Users (username,email,phone) VALUES
('ivan123','ivan@example.com','+380631234567'),
('petro_p','petro@example.com','+380501112233'),
('olena_o','olena@example.com','+380671234890'),
('maria14','maria@example.com','+380991112345'),
('oleg71','oleg@example.com','+380631234568');

-- UsersRoles
INSERT INTO UsersRoles (user_id,role) VALUES
(1,'customer'),(2,'customer'),
(3,'customer'),(4,'admin'),
(5,'customer');

-- Locations
INSERT INTO Locations (name,address,capacity) VALUES
('Central Parking','вул. Головна, 1, Львів',50),
('Airport Parking','Рясне-2, Львів',100),
('Train Station','вул. Чернівецька, Львів',70);

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
(5,'DE5678LS','rented',2);

-- CarStatusHistory
INSERT INTO CarStatusHistory (car_id,status) VALUES
(1,'available'),(2,'available'),
(3,'maintenance'),(4,'available'),
(5,'rented');

-- CarLocationHistory
INSERT INTO CarLocationHistory (car_id,location_id) VALUES
(1,1),(2,1),(3,2),(4,3),(5,2);

-- Rentals
INSERT INTO Rentals (user_id,car_id,location_id,start_date,end_date) VALUES
(1,5,2,'2025-06-10','2025-06-15'),
(2,1,1,'2025-06-12','2025-06-18'),
(3,2,1,'2025-06-05','2025-06-10'),
(5,4,3,'2025-06-14','2025-06-20'),
(1,3,2,'2025-06-20','2025-06-25');


-- Payments
INSERT INTO Payments (rental_id,amount,paid_at) VALUES
(1,250.00,'2025-06-10 09:00:00'),
(2,300.00,'2025-06-12 10:30:00'),
(3,150.00,'2025-06-05 08:45:00'),
(4,200.00,'2025-06-14 11:00:00'),
(5,275.00,'2025-06-20 14:15:00');

-- Fines
INSERT INTO Fines (user_id,rental_id,amount,issued_at,description) VALUES
(1,1,50.00,'2025-06-12','Speeding'),
(2,2,30.00,'2025-06-14','Parking violation'),
(3,3,20.00,'2025-06-07','Red light'),
(5,4,40.00,'2025-06-15','Seatbelt'),
(1,5,60.00,'2025-06-22','Mobile use while driving');




