-- 코드를 입력하세요
-- SELECT NAME FROM (SELECT * FROM ANIMAL_INS ORDER BY DATETIME DESC) WHERE ROWNUM = 1;
SELECT NAME FROM ANIMAL_INS WHERE 1 = 1 AND DATETIME = (SELECT MIN(DATETIME) FROM ANIMAL_INS);