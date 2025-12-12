
USE maksim_rental;

-- Заборонити імена, що закінчуються на 'o'
DROP TRIGGER IF EXISTS trg_users_name_not_o;
DELIMITER $$

CREATE TRIGGER trg_users_name_not_o
BEFORE INSERT ON Users
FOR EACH ROW
BEGIN
  IF RIGHT(NEW.username, 1) = 'o' THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Iм''я користувача не може закінчуватись на \"o\"';
  END IF;
END$$

DELIMITER ;

-- Заборонити букви у полі телефону
DROP TRIGGER IF EXISTS trg_users_phone_only_digits;
DELIMITER $$
CREATE TRIGGER trg_users_phone_only_digits
BEFORE INSERT ON Users
FOR EACH ROW
BEGIN
  IF NEW.phone REGEXP '[a-zA-Z]' THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Телефон не може містити літери';
  END IF;
END$$
DELIMITER ;

-- Заборонити ім'я 'Admin'
DROP TRIGGER IF EXISTS trg_users_no_admin_name;
DELIMITER $$
CREATE TRIGGER trg_users_no_admin_name
BEFORE INSERT ON Users
FOR EACH ROW
BEGIN
  IF LOWER(NEW.username) = 'admin' THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Імя користувача не може бути' "Admin";
  END IF;
END$$
DELIMITER ;
