CREATE DATABASE IF NOT EXISTS maksim_rental;
USE maksim_rental;

-- 1. Таблиця користувачів
CREATE TABLE Users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  phone VARCHAR(20),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 2. Таблиця ролей користувачів (опційно)
CREATE TABLE UsersRoles (
  user_role_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  role VARCHAR(20) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- 3. Таблиця локацій
CREATE TABLE Locations (
  location_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  address VARCHAR(200) NOT NULL,
  capacity INT NOT NULL,
  UNIQUE(name)
);

-- 4. Таблиця моделей авто
CREATE TABLE CarModels (
  model_id INT AUTO_INCREMENT PRIMARY KEY,
  manufacturer VARCHAR(50) NOT NULL,
  model_name VARCHAR(50) NOT NULL,
  engine VARCHAR(50)
);

-- 5. Таблиця автомобілів
CREATE TABLE Cars (
  car_id INT AUTO_INCREMENT PRIMARY KEY,
  model_id INT NOT NULL,
  license_plate VARCHAR(20) NOT NULL UNIQUE,
  current_status ENUM('available','rented','maintenance') NOT NULL DEFAULT 'available',
  current_location_id INT,
  FOREIGN KEY (model_id) REFERENCES CarModels(model_id),
  FOREIGN KEY (current_location_id) REFERENCES Locations(location_id),
  INDEX idx_status (current_status),
  INDEX idx_location (current_location_id)
);

-- 6. Історія статусу авто
CREATE TABLE CarStatusHistory (
  history_id INT AUTO_INCREMENT PRIMARY KEY,
  car_id INT NOT NULL,
  status ENUM('available','rented','maintenance') NOT NULL,
  changed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (car_id) REFERENCES Cars(car_id)
);

-- 7. Історія переміщення авто
CREATE TABLE CarLocationHistory (
  loc_hist_id INT AUTO_INCREMENT PRIMARY KEY,
  car_id INT NOT NULL,
  location_id INT NOT NULL,
  moved_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (car_id) REFERENCES Cars(car_id),
  FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

-- 8. Таблиця фактів оренди
CREATE TABLE Rentals (
  rental_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  car_id INT NOT NULL,
  location_id INT NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (car_id) REFERENCES Cars(car_id),
  FOREIGN KEY (location_id) REFERENCES Locations(location_id),
  INDEX idx_rental_period (start_date, end_date)
);

-- 9. Таблиця оплат
CREATE TABLE Payments (
  payment_id INT AUTO_INCREMENT PRIMARY KEY,
  rental_id INT NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  paid_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (rental_id) REFERENCES Rentals(rental_id)
);

-- 10. Таблиця штрафів
CREATE TABLE Fines (
  fine_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  rental_id INT,
  amount DECIMAL(10,2) NOT NULL,
  issued_at DATE NOT NULL,
  description VARCHAR(255),
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (rental_id) REFERENCES Rentals(rental_id),
  INDEX idx_fine_user (user_id)
);
