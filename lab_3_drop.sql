
-- Безпечне створення БД
DROP DATABASE IF EXISTS maksim_rental;
CREATE DATABASE IF NOT EXISTS maksim_rental;
USE maksim_rental;

-- DROP-таблиці у правильному порядку (щоб уникнути помилок залежностей)
DROP TABLE IF EXISTS Fines;
DROP TABLE IF EXISTS Payments;
DROP TABLE IF EXISTS Rentals;
DROP TABLE IF EXISTS CarLocationHistory;
DROP TABLE IF EXISTS CarStatusHistory;
DROP TABLE IF EXISTS Cars;
DROP TABLE IF EXISTS CarModels;
DROP TABLE IF EXISTS Locations;
DROP TABLE IF EXISTS UsersRoles;
DROP TABLE IF EXISTS Users;

-- Таблиці
CREATE TABLE IF NOT EXISTS Users (
  user_id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(50) NOT NULL UNIQUE,
  email VARCHAR(100) NOT NULL UNIQUE,
  phone VARCHAR(20),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS UsersRoles (
  user_role_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  role VARCHAR(20) NOT NULL,
  FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

CREATE TABLE IF NOT EXISTS Locations (
  location_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  address VARCHAR(200) NOT NULL,
  capacity INT NOT NULL,
  UNIQUE(name)
);

CREATE TABLE IF NOT EXISTS CarModels (
  model_id INT AUTO_INCREMENT PRIMARY KEY,
  manufacturer VARCHAR(50) NOT NULL,
  model_name VARCHAR(50) NOT NULL,
  engine VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Cars (
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

CREATE TABLE IF NOT EXISTS CarStatusHistory (
  history_id INT AUTO_INCREMENT PRIMARY KEY,
  car_id INT NOT NULL,
  status ENUM('available','rented','maintenance') NOT NULL,
  changed_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (car_id) REFERENCES Cars(car_id)
);

CREATE TABLE IF NOT EXISTS CarLocationHistory (
  loc_hist_id INT AUTO_INCREMENT PRIMARY KEY,
  car_id INT NOT NULL,
  location_id INT NOT NULL,
  moved_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (car_id) REFERENCES Cars(car_id),
  FOREIGN KEY (location_id) REFERENCES Locations(location_id)
);

CREATE TABLE IF NOT EXISTS Rentals (
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

CREATE TABLE IF NOT EXISTS Payments (
  payment_id INT AUTO_INCREMENT PRIMARY KEY,
  rental_id INT NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  paid_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (rental_id) REFERENCES Rentals(rental_id)
);

CREATE TABLE IF NOT EXISTS Fines (
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
