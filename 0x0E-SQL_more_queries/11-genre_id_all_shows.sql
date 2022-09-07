-- list all shows contained in hbtn_0d_tvshows
-- if a show doesn't have a genre, display NULL
SELECT s.title, g.genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title ASC, g.genre_id ASC;
