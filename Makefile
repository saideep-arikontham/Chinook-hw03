URL=https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite

group2q1: data/chinook.db
	python -B src/group2q1.py

group2q2: data/chinook.db
	python -B src/group2q2.py

group2q3: data/chinook.db
	python -B src/group2q3.py

group1q1: data/chinook.db
	python -B src/group1q1.py

group1q2: data/chinook.db
	python -B src/group1q2.py

group1q3: data/chinook.db
	python -B src/group1q3.py

group3q1: data/chinook.db
	python -B src/group3q1.py

group3q2: data/chinook.db
	python -B src/group3q2.py

# Plot the histogram
hist: data/chinook.db
	mkdir -p figs
	python -B src/hist.py

# Create the database from the text file with SQL commands
data/chinook.db: data/Chinook_Sqlite.sql
	sqlite3 data/chinook.db < data/Chinook_Sqlite.sql

# Get the SQL to create the database
data/Chinook_Sqlite.sql:
	mkdir -p data
	cd data; curl -LO $(URL).sql

clean:
	rm data/*
