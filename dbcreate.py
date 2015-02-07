#!/usr/bin/env python

import sqlite3
import sys

season = sys.argv[1]
filename = "osm%i%i.db" % (int(season[2:]), int(season[2:]) + 1)

connection = sqlite3.connect(filename)
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys=on")

# About
cursor.execute("CREATE TABLE IF NOT EXISTS about (season INTEGER, version INTEGER)")
cursor.execute("INSERT INTO about VALUES (2014, 1)")

# Stadium
cursor.execute("CREATE TABLE IF NOT EXISTS stadium (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, north INTEGER, east INTEGER, south INTEGER, west INTEGER, northeast INTEGER, northwest INTEGER, southeast INTEGER, southwest INTEGER, northbox INTEGER, eastbox INTEGER, southbox INTEGER, westbox INTEGER, northroof INTEGER, eastroof INTEGER, southroof INTEGER, westroof INTEGER, northeastroof INTEGER, northwestroof INTEGER, southeastroof INTEGER, southwestroof INTEGER, northseating INTEGER, eastseating INTEGER, southseating INTEGER, westseating INTEGER, northeastseating INTEGER, northwestseating INTEGER, southeastseating INTEGER, southwestseating INTEGER, stall INTEGER, programme INTEGER, smallshop INTEGER, largeshop INTEGER, bar INTEGER, burgerbar INTEGER, cafe INTEGER, restaurant INTEGER)")

# Club
cursor.execute("CREATE TABLE IF NOT EXISTS club (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, nickname TEXT, manager TEXT, chairman TEXT, stadium INTEGER, reputation INTEGER, FOREIGN KEY(stadium) REFERENCES stadium(id))")

# Nation
cursor.execute("CREATE TABLE IF NOT EXISTS nation (id INTEGER PRIMARY KEY AUTOINCREMENT, nation TEXT, denonym TEXT)")

# Companies
cursor.execute("CREATE TABLE IF NOT EXISTS company (name TEXT)")

# Player
cursor.execute("CREATE TABLE IF NOT EXISTS player (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, secondname TEXT, commonname TEXT, dateofbirth TEXT, club INTEGER, nation INTEGER, position TEXT, keeping INTEGER, tackling INTEGER, passing INTEGER, shooting INTEGER, heading INTEGER, pace INTEGER, stamina INTEGER, ballcontrol INTEGER, setpieces INTEGER, training INTEGER, FOREIGN KEY(club) REFERENCES club(id), FOREIGN KEY(nation) REFERENCES nation(id))")

# Injury
cursor.execute("CREATE TABLE IF NOT EXISTS injury (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, minperiod INTEGER, maxperiod INTEGER, minfitness INTEGER, maxfitness INTEGER)")

# Suspension
cursor.execute("CREATE TABLE IF NOT EXISTS suspension (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, minimum INTEGER, maximum INTEGER)")

# Referee
cursor.execute("CREATE TABLE IF NOT EXISTS referee (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

# Staff
cursor.execute("CREATE TABLE IF NOT EXISTS staff (name TEXT)")

# Buildings
cursor.execute("CREATE TABLE IF NOT EXISTS buildings (name TEXT, plot INTEGER, cost INTEGER)")

# Merchandise
cursor.execute("CREATE TABLE IF NOT EXISTS merchandise (name TEXT, cost INTEGER, multiplier INTEGER)")

# Catering
cursor.execute("CREATE TABLE IF NOT EXISTS catering (name TEXT, cost INTEGER, multiplier INTEGER)")

connection.commit()

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

# Referee
print("Referee")
fp = open("referee.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO referee VALUES (null, ?)", (line))

# Staff
print("Staff")
fp = open("staff.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    if item != "":
        cursor.execute("INSERT INTO staff VALUES (?)", (item,))

# Nation
print("Nation")
fp = open("nation.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO nation VALUES (?, ?, ?)", (line))

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

# Stadium
print("Stadium")
fp = open("stadium.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO stadium VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (line))

# Club
print("Club")
fp = open("club.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO club VALUES (?, ?, ?, ?, ?, ?, ?)", (line))

# Player
print("Player")
fp = open("player.csv")

data = fp.read()
data = data.split("\n")

for item in data:
    line = item.split(",")

    if line != [""]:
        cursor.execute("INSERT INTO player VALUES (null, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (line))

connection.commit()
connection.close()
