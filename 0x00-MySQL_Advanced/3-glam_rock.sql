-- An SQL script that lists all bands with Glam rock as their main style
-- Using attributes formed and spilit for computing the lifespan

SELECT band_name,
	CASE 
		WHEN split is NOT NULL THEN (split - formed)
		ELSE (2022 - formed)
	END AS lifespan
FROM
	metal_bands
WHERE
	style = 'Glam rock'
ORDER BY
	lifespan DESC;
