# A built-in Swiss system tournament
Udacity - implementation of a Swiss-system tournament

## Project Description
The goal of the Swiss pairings system is to pairing up player in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

## Requirements
If you want to run the program you have to have [Python ~2.7](https://www.python.org/)
and [PostgreSQL](http://www.postgresql.org/) installed on your machine.

## Set Up

For an initial set up please follow these 3 steps:

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).

2. Clone the [fullstack-nanodegree-vm repository](http://github.com/udacity/fullstack-nanodegree-vm). Open folder from that repository and replace the files inside the *tournament* folder.

3. Install git-bash command line terminal  (https://git-scm.com/downloads)

3. Open  git-bash terminal and locate *vagrant* folder for our command line. Use command:
`cd \ ..your path..\ vagrant`


## Usage

Launch the Vagrant VM from inside the *vagrant* folder from git-bash command line:

`vagrant up`

`vagrant ssh`

Execute the following commands to create the necessary tables inside the database:

`cd /vagrant/tournament`

`psql -f tournament.sql`

Execute the following command to run the test and see the output from your console:

`python tournament_test.py`

# Expect result if all runs well you receive the following message:

1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
