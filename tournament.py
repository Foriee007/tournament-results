#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import itertools


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    # Set up use of the connect() method help to  avoid code repetition.
    # Set up  the connection to  DB  with the cursor for assign and return
    # multiple variables simultaneously.
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        # Show Error on connection failure.
        print("Error connecting to the database.")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    query = "TRUNCATE matches;"
    cursor.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    query = "DELETE FROM players;"
    cursor.execute(query)
    # After deleting, fuction should return numeric zero
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = "SELECT COUNT(*) AS total FROM players;"
    cursor.execute(query)
    total = cursor.fetchone()
    # After one player registers, fuction should be 1
    db.close()
    return total[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    """Returns the number of players currently registered."""
    db, cursor = connect()
    query = "INSERT INTO players (name) VALUES (%s);"
    param = (name,)
    cursor.execute(query, param)

    db.commit()
    db.close()
    return countPlayers()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, cursor = connect()
    query = "SELECT * FROM gamecounter;"
    cursor.execute(query)
    playerslist = cursor.fetchall()

    if (playerslist[0][2] != 0) and (playerslist[0][2] == playerslist[1][2]):
        query = "SELECT player_id, player_name, wins, games " \
                "FROM gamecounter "\
                "ORDER BY (cast(wins AS DECIMAL)/games) DESC;"
        cursor.execute(query)
        playerslist = cursor.fetchall()
    db.close()

    return playerslist


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    # query = "update players set wins = 1 where id = %s;"
    # data = (winner,)
    # cursor.execute(query, data)
    # query = "update players set matches = 1 where id = %s or id = %s;"
    # data = (winner, loser)
    # cursor.execute(query, data)
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    param = (winner, loser,)
    cursor.execute(query, param)
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db, cursor = connect()
    query = "SELECT * FROM gamecounter"
    cursor.execute(query)
    results = cursor.fetchall()
    pairings = []
    count = len(results)

    for x in range(0, count - 1, 2):
        paired_list = (results[x][0], results[x][1], results[x + 1][0], results[x + 1][1])  # noqa
        pairings.append(paired_list)

    db.close()
    return pairings
