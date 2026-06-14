SELECT user_id, sum(amount) as total_spent
FROM user_purchases
GROUP BY user_id
