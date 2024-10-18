-- An SQL script that lists all bands with Glam rock as their main style
-- Using attributes formed and spilit for computing the lifespan

DELIMITER $$

CREATE FUNCTION calculate_lifespan(formed INT, split INT)
RETURNS INT DETERMINISTIC
BEGIN
	DECLARE lifespan INT;
	SET lifespan = IFNULL(split,  2022) - formed;
	RETURN lifespan;
END;

DELIMITER;


SELECT band_name,
calculate_lifespan(formed,split) AS longevity
FROM bands
WHERE main_style = 'Glam rock'
ORDER BY longevity DESC;
