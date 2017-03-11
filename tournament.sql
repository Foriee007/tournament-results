-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
-- 
-- Clear out any previous tournament databases.
DROP DATABASE IF EXISTS tournament;

-- Create database and connect to the DB before creating tables

CREATE DATABASE tournament;
\c tournament;

-- Create table for players.

CREATE TABLE players (
  id serial PRIMARY KEY,
  name text NOT NULL
);

-- Create table for games.

CREATE TABLE matches (
  match_id serial PRIMARY KEY,
  winner int,
  loser int,
  FOREIGN KEY(winner) REFERENCES players(id),
  FOREIGN KEY(loser) REFERENCES players(id)
);

-- Create view to show games standings.

CREATE VIEW gamecounter
AS
SELECT players.id AS player_id, players.name AS player_name,
(SELECT count(*) FROM matches WHERE matches.winner = players.id) AS wins,
(SELECT count(*) FROM matches WHERE players.id in (winner, loser)) AS games
FROM players
GROUP BY players.id, players.name
ORDER BY wins DESC;
