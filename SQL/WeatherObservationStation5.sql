/*
Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

Sample Input
For example, CITY has four entries: DEF, ABC, PQRS and WXY.

Explanation
When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with lengths  and . The longest name is PQRS, but there are  options for shortest named city. Choose ABC, because it comes first alphabetically.
Note
You can write two separate queries to get the desired output. It need not be a single query.
*/

WITH city_lenghts AS (
    SELECT city, CHAR_LENGTH(city) AS char_count
    FROM station
),
max_city AS(
    SELECT city, char_count
    FROM city_lenghts
    WHERE char_count = (SELECT MAX(char_count) FROM city_lenghts)
    ORDER BY city asc
    LIMIT 1
),
min_city AS(
    SELECT city, char_count
    from city_lenghts
    WHERE char_count = (SELECT MIN(char_count) FROM city_lenghts)
    ORDER BY city asc
    LIMIT 1
)
SELECT * 
FROM max_city
UNION ALL
SELECT *
FROM min_city