-- name: save_quote
INSERT INTO quotes (quotes, author) VALUES (%s, %s)

-- name: show_saved_quote
SELECT * FROM quotes