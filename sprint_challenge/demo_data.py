"""This file is for Part 1 of the Unit 3 Sprint 2 Challenge"""

# Import Libraries
import sqlite3


# Open a connection to demo_data
def open_connection(db):
    con = sqlite3.connect(db)
    return con


# This function is to create a table AND to instert data
def create_table(cur, query):
    return cur.execute(query)


# This functions is to execute queries
def execute_query(cur, query):
    return cur.execute(query).fetchall()


# Queries
DEMO = """CREATE TABLE demo (
                s VARCHAR,
                x INT,
                y INT
                );"""

INSERT = """INSERT INTO demo (s, x, y)
            VALUES
                ("g", 3, 9),
                ("v", 5, 7),
                ("f", 8, 7);"""

row_count = """SELECT count(*) FROM demo"""

xy_at_least_5 = """SELECT count(*)
                     FROM demo
                    WHERE x >= 5
                      AND y > 5"""

unique_y = """SELECT count(DISTINCT y) FROM demo"""


if __name__ == "__main__":
    # This Creates and Commits the Table
    sq_con = open_connection('demo_data.sqlite3')
    sq_cur = sq_con.cursor()
    create_table(sq_cur, DEMO)
    create_table(sq_cur, INSERT)
    sq_con.commit()

    # The functions below execute queries
    rows = execute_query(sq_cur, row_count)
    xy = execute_query(sq_cur, xy_at_least_5)
    uy = execute_query(sq_cur, unique_y)

    # Print Results
    print(rows)  # Answer: 3
    print(xy)  # Answer: 2
    print(uy)  # Answer: 2

    # Clean up time
    sq_cur.close()
    sq_con.close()
