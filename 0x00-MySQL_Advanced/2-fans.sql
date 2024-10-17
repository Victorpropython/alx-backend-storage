-- A script to rank country of bands, ordered by the number of
-- (non unique fan) and it will be imported from a dump

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
