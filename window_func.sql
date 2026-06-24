-- SELECT user_id, sum(amount) as total_spent
-- FROM user_purchases
-- GROUP BY user_id

-- SELECT users.name, transactions.txn_id, amount
-- FROM users
-- join transactions ON users.user_id = transactions.user_id

-- SELECT users.name, sum(amount) as total_spent
-- FROM users
-- join transactions ON users.user_id = transactions.user_id
-- GROUP BY users.user_id, users.name

-- SELECT users.name, sum(amount) as total_spent
-- FROM users
-- join transactions ON users.user_id = transactions.user_id
-- GROUP BY users.user_id, users.name
-- having total_spent > 1000

with RankedApplications AS (
    SELECT  
        user_id,
        vacancy_id,
        ROW NUMBER() OVER(PARTITION BY user_id ORDER BY created_at DESC) as rn
    FROM applications
)

SELECT user_id, vacancy_id
FROM RankedApplications
where rn = 1;