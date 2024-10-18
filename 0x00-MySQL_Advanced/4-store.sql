-- An SQL script to crete a Trigger that decreases the quantity
-- of an item after adding a new order.
-- Quantity in the table items can be negative.
DELIMITER $$

CREATE TRIGGER decrease_item
AFTER INSERT ON orders
FOR EACH ROW
	BEGIN
		-- Decreasing the items
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE items.name = NEW.item_name;
	END$$

DELIMITER;

