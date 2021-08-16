# Import Libraries

import sqlite3


# Connect to the Database
def open_connection(db):
    con = sqlite3.connect(db)
    return con


# This functions is to execute queries
def execute_query(cur, query):
    return cur.execute(query).fetchall()


# Queries
expensive_items = """SELECT *
                       FROM Product
                   ORDER BY UnitPrice DESC
                      LIMIT 10;"""

avg_hire_age = """SELECT AVG(HireDate - BirthDate)
                    FROM Employee;"""

avg_age_by_city = """SELECT City, AVG(HireDate - BirthDate)
                       FROM Employee
                   GROUP BY City;"""

# Note that this query returns the 10 most expensive products
# that have suppliers listed And not the absolute 10 most expensive products
ten_most_expensive = """SELECT ProductName, UnitPrice, CompanyName
                          FROM Product
                          JOIN Supplier
                            ON Product.Id = Supplier.Id
                      ORDER BY UnitPrice DESC
                         LIMIT 10;"""

largest_category = """SELECT DISTINCT CategoryId, count(CategoryId)
                        FROM Product
                    GROUP BY CategoryId
                    ORDER BY count(CategoryId) DESC;"""

most_territories = """SELECT EmployeeId, FirstName, LastName, count(TerritoryId)
                        FROM Employee
                        JOIN EmployeeTerritory
                          ON Employee.Id = EmployeeTerritory.EmployeeId
                    GROUP BY EmployeeId
                    ORDER BY count(TerritoryId) DESC;"""

if __name__ == "__main__":
    # Open a connection and a cursor
    sq_con = open_connection("""C:/Users/lsisl/DS-Unit-3-Sprint-2-SQL-and-Databases/
    sprint_challenge/Northwind_small.sqlite""")
    sq_cur = sq_con.cursor()

    # Execute your queries
    expensive = execute_query(sq_cur, expensive_items)
    avg_hire = execute_query(sq_cur, avg_hire_age)
    avg_stretch_goal = execute_query(sq_cur, avg_age_by_city)
    ten_big_money = execute_query(sq_cur, ten_most_expensive)
    max_category = execute_query(sq_cur, largest_category)
    max_territories = execute_query(sq_cur, most_territories)

    # Print Results
    print(expensive)
    print(avg_hire)  # ANSWER: 37.2
    print(avg_stretch_goal)
    print(ten_big_money)
    print(max_category)  # ANSWER: 3
    print(max_territories)  # ANSWER EMPLOYEE ID 7 ROBERT

    # Clean up
    sq_cur.close()
    sq_con.close()
