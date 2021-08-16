# 1. Import libraries
import pandas as pd
import numpy as np
import sqlite3

# 2. Read the .csv into a DataFrame
df = pd.read_csv('buddymove_holidayiq.csv')

# 3. Create a Connection to the Database
con = sqlite3.connect('buddymove_holidayiq.sqlite3')

# 4. Insert the DataFrame into the table you created above
df.to_sql('buddymove_holidayiq', con)

# 5. Open a cursor
cur = con.cursor()

# 6. Count how many rows you have
ROWS = cur.execute('SELECT count(*) FROM buddymove_holidayiq').fetchone()

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
USERS = cur.execute("""SELECT count(*)
                         FROM buddymove_holidayiq
                        WHERE Nature >= 100
                          AND Shopping >= 100;""").fetchone()

# Stretch Goal What are the average number of reviews for each category?
AVG_Sports = cur.execute("""SELECT AVG(Sports)
                              FROM buddymove_holidayiq;""").fetchone()

AVG_Religious = cur.execute("""SELECT AVG(Religious)
                              FROM buddymove_holidayiq;""").fetchone()

AVG_Nature = cur.execute("""SELECT AVG(Nature)
                              FROM buddymove_holidayiq;""").fetchone()

AVG_Theatre = cur.execute("""SELECT AVG(Theatre)
                              FROM buddymove_holidayiq;""").fetchone() 

AVG_Shopping = cur.execute("""SELECT AVG(Shopping)
                              FROM buddymove_holidayiq;""").fetchone() 

AVG_Picnic = cur.execute("""SELECT AVG(Picnic)
                              FROM buddymove_holidayiq;""").fetchone()   

# 7. Close Cursor and Connection 
cur.close()
con.close()                                                                                                                 
