#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect("opensoccermanager.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys=on")

cursor.execute("CREATE TABLE IF NOT EXISTS staff (name TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS year (year INTEGER PRIMARY KEY NOT NULL)")

cursor.execute("CREATE TABLE IF NOT EXISTS company (name TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS nation (id INTEGER PRIMARY KEY, name, denonym)")

cursor.execute("CREATE TABLE IF NOT EXISTS league (id INTEGER PRIMARY KEY NOT NULL, name TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS leagueattr (id INTEGER PRIMARY KEY AUTOINCREMENT, league INTEGER NOT NULL, year INTEGER NOT NULL, FOREIGN KEY(league) REFERENCES league(id), FOREIGN KEY(year) REFERENCES year(year))")

cursor.execute("CREATE TABLE IF NOT EXISTS stadium (id INTEGER PRIMARY KEY NOT NULL, name TEXT)")

cursor.execute("CREATE TABLE IF NOT EXISTS stadiumattr (id INTEGER PRIMARY KEY AUTOINCREMENT, stadium INTEGER NOT NULL, year INTEGER NOT NULL, north INTEGER, east INTEGER, south INTEGER, west INTEGER, northeast INTEGER, northwest INTEGER, southeast INTEGER, southwest INTEGER, northbox INTEGER, eastbox INTEGER, southbox INTEGER, westbox INTEGER, northroof INTEGER, eastroof INTEGER, southroof INTEGER, westroof INTEGER, northeastroof INTEGER, northwestroof INTEGER, southeastroof INTEGER, southwestroof INTEGER, northseating INTEGER, eastseating INTEGER, southseating INTEGER, westseating INTEGER, northeastseating INTEGER, northwestseating INTEGER, southeastseating INTEGER, southwestseating INTEGER, stall INTEGER, programme INTEGER, smallshop INTEGER, largeshop INTEGER, bar INTEGER, burgerbar INTEGER, cafe INTEGER, restaurant INTEGER, FOREIGN KEY(stadium) REFERENCES stadium(id))")

cursor.execute("CREATE TABLE IF NOT EXISTS club (id INTEGER PRIMARY KEY NOT NULL, name, nickname)")

cursor.execute("CREATE TABLE IF NOT EXISTS clubattr (id INTEGER PRIMARY KEY AUTOINCREMENT, club INTEGER NOT NULL, year INTEGER NOT NULL, league INTEGER, manager, chairman, stadium INTEGER, reputation INTEGER, FOREIGN KEY(club) REFERENCES club(id), FOREIGN KEY(year) REFERENCES year(year), FOREIGN KEY(stadium) REFERENCES stadium(id), FOREIGN KEY(league) REFERENCES league(id))")

cursor.execute("CREATE TABLE IF NOT EXISTS player (id INTEGER PRIMARY KEY NOT NULL, firstname, secondname, commonname, dateofbirth, nation INTEGER, FOREIGN KEY(nation) REFERENCES nation(id))")

cursor.execute("CREATE TABLE IF NOT EXISTS playerattr (id INTEGER PRIMARY KEY AUTOINCREMENT, player INTEGER NOT NULL, year INTEGER NOT NULL, club INTEGER, position, keeping INTEGER, tackling INTEGER, passing INTEGER, shooting INTEGER, heading INTEGER, pace INTEGER, stamina INTEGER, ballcontrol INTEGER, setpieces INTEGER, training INTEGER, FOREIGN KEY(player) REFERENCES player(id), FOREIGN KEY(club) REFERENCES club(id), FOREIGN KEY(year) REFERENCES year(year))")

cursor.execute("CREATE TABLE IF NOT EXISTS injury (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, minperiod INTEGER, maxperiod INTEGER, minfitness INTEGER, maxfitness INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS suspension (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, minimum INTEGER, maximum INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS buildings (name TEXT, plot INTEGER, cost INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS merchandise (name TEXT, cost INTEGER, multiplier INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS catering (name TEXT, cost INTEGER, multiplier INTEGER)")

cursor.execute("CREATE TABLE IF NOT EXISTS referee (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, league INTEGER, year INTEGER NOT NULL, FOREIGN KEY(year) REFERENCES year(year), FOREIGN KEY(league) REFERENCES league(id))")


# Staff
print("Staff")
fp = open("staff.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    if item != "":
        cursor.execute("INSERT INTO staff VALUES (?)", (item,))

# Year
print("Year")
for year in (2001, 2014, 2015):
    cursor.execute("INSERT INTO year VALUES (?)", (year,))

# Injury
print("Injury")
fp = open("injury.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO injury VALUES (null, ?, ?, ?, ?, ?)", (line))

# Suspension
print("Suspension")
fp = open("suspension.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO suspension VALUES (?, ?, ?, ?)", (line))

# Nation
print("Nation")
fp = open("nation.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO nation VALUES (?, ?, ?)", (line))

# League
print("League")
fp = open("league.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO league VALUES (?, ?)", (line))

print("LeagueAttr")
fp = open("leagueattr.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO leagueattr VALUES (?, ?, ?)", (line))

# Stadium
print("Stadium")
fp = open("stadium.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO stadium VALUES (?, ?)", (line))

print("StadiumAttr")
fp = open("stadiumattr.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO stadiumattr VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (line))

# Club
print("Club")
fp = open("club.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO club VALUES (?, ?, ?)", (line))

print("ClubAttr")
fp = open("clubattr.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO clubattr VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (line))

# Player
print("Player")
fp = open("player.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO player VALUES (?, ?, ?, ?, ?, ?)", (line))

print("PlayerAttr")
fp = open("playerattr.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO playerattr VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (line))

# Company
print("Company")
fp = open("company.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO company VALUES (?)", (line))

# Buildings
print("Buildings")
fp = open("buildings.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO buildings VALUES (?, ?, ?)", (line))

# Merchandise
print("Merchandise")
fp = open("merchandise.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO merchandise VALUES (?, ?, ?)", (line))

# Catering
print("Catering")
fp = open("catering.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO catering VALUES (?, ?, ?)", (line))

# Referee
print("Referee")
fp = open("referee.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO referee VALUES (null, ?, ?, ?)", (line))

connection.commit()
connection.close()
