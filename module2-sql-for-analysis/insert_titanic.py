# 1. Import Libraries 
import sqlite3
import psycopg2

# 2. Create Connection to sqlite3
s_conn = sqlite3.connect('titanic_db.sqlite3')

# 3. Open a Cursor 
s_cur = s_conn.cursor()


# 4. Create Connection to posgreSQL on ElephantSQL
dbname = "enfizahe"
user = "enfizahe"
password = "FDV_F8Q09YEiKHw0XcMm09eBe2HrjQpy"
host = "chunee.db.elephantsql.com"

con = psycopg2.connect(dbname= dbname, user= user, password = password, host= host)

con 

# 5. Create Cursor

p_cur = con.cursor()

# 6. Create Table

p_cur.execute("""
            CREATE TABLE titanic (
                id SERIAL PRIMARY KEY,
                survived BOOL,
                pclass INTEGER,
                name VARCHAR(150) NOT NULL,
                sex VARCHAR(10) NOT NULL,
                age FLOAT,
                sib_spouse INTEGER,
                parent_children INTEGER,
                fare FLOAT)
            """)
# 7. Create Column Names

columns = ('survived', 'pclass', 'name', 'sex', 'age', 'sib_spouse', 'parent_children', 'fare')

# 8. Copy From CSV to PostgreSQL Table (delete header from .csv file)

f = open(r'C:/Users/lsisl/DS-Unit-3-Sprint-2-SQL-and-Databases/module2-sql-for-analysis/titanic.csv', 'r')

p_cur.copy_from(f, 'titanic', sep= ',', columns= columns)

#9. Commit to Database

con.commit()

#10. Close Cursors and Connections
s_conn.close()
con.close()
s_cur.close()
p_cur.close()


