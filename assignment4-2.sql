CREATE EXTENSION IF NOT EXISTS citext;
ALTER TABLE track
ALTER COLUMN name TYPE citext;
CREATE INDEX idx_track_name ON track (name);
SELECT album.title
FROM track
JOIN album ON track.album_id = album.album_id
WHERE track.name = 'Enter Sandman';