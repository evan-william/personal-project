-- name: add_collection
INSERT INTO book_collections (title, author) VALUES (%s, %s);

-- name: remove_collection
DELETE FROM book_collections WHERE title = %s;

-- name: list_collections
SELECT * FROM book_collections;
