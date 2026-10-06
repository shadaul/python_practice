WITH RankedEvents AS (
    SELECT
        user_id,
        event_type,
        event_time,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, event_type
            ORDER BY event_time DESC
        ) as rn
    FROM raw_user_events
)
SELECT user_id,
    COUNT(*) as total_events
FROM RankedEvents
WHERE rn = 1
GROUP BY user_id
ORDER BY total_events DESC;