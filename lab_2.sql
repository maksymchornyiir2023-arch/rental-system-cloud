
#1
SELECT ship, battle, result
FROM Outcomes
WHERE battle = 'Guadalcanal' AND result <> 'sunk'
ORDER BY ship DESC;

#2

SELECT name, launched
FROM Ships
WHERE name NOT LIKE '%a';

#3

SELECT Product.maker, PC.model, PC.price
FROM Product
JOIN PC ON Product.model = PC.model;

#4

SELECT DISTINCT maker
FROM Product
WHERE type = 'PC'
AND model NOT IN (SELECT DISTINCT model FROM PC);

#5

SELECT Ships.name, Ships.launched, Classes.displacement
FROM Ships
JOIN Classes ON Ships.class = Classes.class
WHERE launched >= 1922 AND displacement > 35000;

#6

SELECT 
  CONCAT('код: ', code) AS code,
  CONCAT('модель: ', model) AS model,
  CONCAT('колір: ', color) AS color,
  CONCAT('тип: ', type) AS type,
  CONCAT('ціна: ', FORMAT(price, 2)) AS price
FROM Printer;

#7

SELECT maker
FROM Product
WHERE type = 'PC'
GROUP BY maker
HAVING COUNT(*) = (
  SELECT COUNT(DISTINCT model)
  FROM Product p2
  WHERE p2.maker = Product.maker AND type = 'PC' AND model IN (SELECT model FROM PC)
);


#8

SELECT 
  ship,
  (SELECT displacement FROM Classes WHERE Classes.class = Ships.class) AS displacement,
  (SELECT numGuns FROM Classes WHERE Classes.class = Ships.class) AS numGuns
FROM Outcomes
JOIN Ships ON Outcomes.ship = Ships.name
WHERE battle = 'Guadalcanal';

#9

SELECT 
  Trip.trip_no,
  Company.name AS company_name,
  Trip.plane,
  Trip.town_from,
  Trip.town_to,
  CASE 
    WHEN TIMESTAMPDIFF(MINUTE, time_out, time_in) < 0 THEN 
      CONCAT(FLOOR((1440 + TIMESTAMPDIFF(MINUTE, time_out, time_in)) / 60), 'h ', 
             (1440 + TIMESTAMPDIFF(MINUTE, time_out, time_in)) % 60, 'm')
    ELSE 
      CONCAT(FLOOR(TIMESTAMPDIFF(MINUTE, time_out, time_in) / 60), 'h ', 
             TIMESTAMPDIFF(MINUTE, time_out, time_in) % 60, 'm')
  END AS flight_duration
FROM Trip
JOIN Company ON Trip.ID_comp = Company.ID_comp;


#10

SELECT AVG(price) AS avg_price
FROM (
  SELECT price FROM PC JOIN Product ON PC.model = Product.model WHERE maker = 'A'
  UNION ALL
  SELECT price FROM Laptop JOIN Product ON Laptop.model = Product.model WHERE maker = 'A'
) AS all_products;


# Запити до моєї бд

#1 

SELECT * FROM Users;


#2

SELECT username, COUNT(*) AS rental_count
FROM Users u
JOIN Rentals r ON u.user_id = r.user_id
GROUP BY u.user_id;

#3

SELECT l.name AS location_name, COUNT(c.car_id) AS car_count
FROM Locations l
LEFT JOIN Cars c ON l.location_id = c.current_location_id
GROUP BY l.location_id;

#4

SELECT * FROM Fines
WHERE amount > 40;

#5

SELECT * FROM Payments
ORDER BY amount DESC;

