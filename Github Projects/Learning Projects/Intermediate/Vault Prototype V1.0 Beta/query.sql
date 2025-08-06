<code class="sql">
-- query.sql

-- name: start_session
INSERT INTO Sessions (user_id, task, deadline, offered_balance, witness, charity)
VALUES (%s, %s, %s, %s, %s, %s);

-- name: show_total_donation
SELECT id, donation FROM User;

-- name: register_new_user
INSERT INTO User (username, password, balance, donation) VALUES (%s, %s, 0.00, 0.00);

-- name: find_user_by_username
SELECT id, username, password, balance, donation FROM User WHERE username = %s;

-- name: find_user_by_id
SELECT id, username, password, balance, donation FROM User WHERE id = %s;

-- name: add_to_balance
UPDATE User SET balance = balance + %s WHERE id = %s;

-- name: get_sessions_by_user
SELECT * FROM Sessions WHERE user_id = %s ORDER BY deadline ASC;

-- name: get_session_by_id
SELECT * FROM Sessions WHERE id = %s;

-- name: get_expired_pending_sessions_by_user
SELECT id, offered_balance FROM Sessions WHERE user_id = %s AND status = 'pending' AND deadline < CURDATE();

-- name: update_session_status
UPDATE Sessions SET status = %s WHERE id = %s;

-- name: add_to_donation
UPDATE User SET donation = donation + %s WHERE id = %s;
```