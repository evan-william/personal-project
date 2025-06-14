-- name: save_win_ai
UPDATE wininfo
SET AiWin = AiWin + 1
WHERE id = 1;

-- name: save_win_human
UPDATE wininfo
SET UserWin = UserWin + 1
WHERE id = 1;

-- name: show_win
SELECT * FROM wininfo
WHERE id = 1;