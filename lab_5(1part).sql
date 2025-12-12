USE maksim_rental;

-- Таблиця нотаток користувачів
DROP TABLE IF EXISTS UserNotes;

CREATE TABLE UserNotes (
  note_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  note_text TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Тригер для INSERT
DROP TRIGGER IF EXISTS trg_insert_note_user_exists;

DELIMITER $$
CREATE TRIGGER trg_insert_note_user_exists
BEFORE INSERT ON UserNotes
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = NEW.user_id) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'User does not exist';
  END IF;
END$$
DELIMITER ;

-- Тригер для UPDATE
DROP TRIGGER IF EXISTS trg_update_note_user_exists;

DELIMITER $$
CREATE TRIGGER trg_update_note_user_exists
BEFORE UPDATE ON UserNotes
FOR EACH ROW
BEGIN
  IF NOT EXISTS (SELECT 1 FROM Users WHERE user_id = NEW.user_id) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'User does not exist for update';
  END IF;
END$$
DELIMITER ;
