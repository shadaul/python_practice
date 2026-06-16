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

