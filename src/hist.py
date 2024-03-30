import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Create the database connection
con = sqlite3.connect('data/chinook.db')
cur = con.cursor()

# Print all the table names
query = "SELECT name FROM sqlite_master WHERE type='table';"
cur.execute(query)
for row in cur:
    print(row[0])

# Get all the song durations (in minutes)
query = "SELECT Milliseconds FROM Track;"
cur.execute(query)
duration = []
for row in cur:
    duration.append(row[0] / 1000 / 60)

# Plot the histogram with a bin with of 10/6 minutes = 100 seconds
print(f"min duration: {min(duration):.2f} minutes")
print(f"max duration: {max(duration):.2f} minutes")
plt.hist(duration, bins=np.arange(min(duration), max(duration), 10/6))

plt.savefig("figs/hist.png")
plt.show() 
