-- name: register_input
INSERT INTO users (username, password, highscore) VALUES (%s, %s, %s)

-- name: login_input
SELECT username, highscore FROM users WHERE username = %s AND password = %s