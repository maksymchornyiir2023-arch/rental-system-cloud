USE maksim_rental;

DELIMITER //

DROP PROCEDURE IF EXISTS CalculateAggregate//

CREATE PROCEDURE CalculateAggregate(
    IN p_table_name VARCHAR(100),
    IN p_column_name VARCHAR(100),
    IN p_operation VARCHAR(10)
)
BEGIN
    SET @sql = CONCAT('SELECT ', p_operation, '(', p_column_name, ') AS result FROM ', p_table_name);
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END//

DELIMITER ;