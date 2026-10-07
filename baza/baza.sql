-- WITH RankedEvents AS (
--     SELECT
--         user_id,
--         event_type,
--         event_time,
--         ROW_NUMBER() OVER (
--             PARTITION BY user_id, event_type
--             ORDER BY event_time DESC
--         ) as rn
--     FROM raw_user_events
-- )
-- SELECT user_id,
--     COUNT(*) as total_events
-- FROM RankedEvents
-- WHERE rn = 1
-- GROUP BY user_id
-- ORDER BY total_events DESC;

SELECT
    u.name,
    sum(o.amount) AS total_spent 
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name 
HAVING sum(o.amount) > 500
ORDER BY total_spent DESC;