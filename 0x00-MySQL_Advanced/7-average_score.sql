-- An SQL  script that creates a stored procedure ComputeAverageScoreForUser 
-- that computes and store the average score for a student.
-- note An average score can be a decimal

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_score DECIMAL(5, 2);

	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE user_id = user_id;

	IF NOT EXISTS CREATE (SELECT 1 FROM average_score WHERE user_id = user_id) THEN

		UPDATE average_score
		SET avg_score = avg_score
		WHERE user_id = user_id;
	ELSE
		INSERT INTO average_score (user_id, avg_score)
		VALUES (user_id, avg_score);
	END IF;

END $$

DELIMITER;
