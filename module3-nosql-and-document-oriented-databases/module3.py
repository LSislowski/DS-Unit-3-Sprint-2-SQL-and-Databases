"""An example of how to import the character table into MongoDB from SQLite"""

# Import Packages
import pymongo
import sqlite3




# Connect to Mongo

def create_mdb_connection(password, dbname):
    client = pymongo.MongoClient(
        "mongodb+srv://playerone:{}@cluster0.1e53z.mongodb.net/{}?retryWrites=true&w=majority"
        .format(password, dbname)
    )
    return client

# Connect to the database you are extracting FROM

def create_sl_conn(extraction_db="C:/Users/lsisl/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(extraction_db)
    return sl_conn

# Use This to Execute Queries and call your rows

def execute_query(curs, query):
    return curs.execute(query).fetchall()

# Each Function below will call a different table into the MongoDB
def doc_creation_character(db):
    character_table = []
    character_columns = ['id','name', 'level', 'exp', 'hp', 'strength', 'intelligence', 'dex', 'wisdom']
    GET_CHARACTERS = "SELECT * FROM charactercreator_character;"
    character_rows = execute_query(sl_curs, GET_CHARACTERS)
    for row in character_rows:
        character_table.append({x:y for x,y in zip(character_columns, row)})

    return db.charactercreator_character.insert_many(character_table)

def doc_creation_inventory(db):
    inventory_table = []
    inventory_columns = ['id', 'item']
    GET_INVENTORY = "SELECT character_id, item_id FROM charactercreator_character_inventory;"
    inventory_rows = execute_query(sl_curs, GET_INVENTORY)
    for row in inventory_rows:
        inventory_table.append({x:y for x,y in zip(inventory_columns, row)})
        
    return db.charactercreator_character_inventory.insert_many(inventory_table)    

def doc_creation_items(db):
    items_table = []
    items_columns = ['item', 'name', 'value', 'weight']
    GET_ITEMS = "SELECT * FROM armory_item;"
    items_rows = execute_query(sl_curs, GET_ITEMS)
    for row in items_rows:
        items_table.append({x:y for x,y in zip(items_columns, row)})
        
    return db.armory_item.insert_many(items_table)      

def doc_creation_weapons(db):
    weapons_table = []
    weapons_columns = ['item', 'power']
    GET_WEAPONS = "SELECT * FROM armory_weapon;"
    weapons_rows = execute_query(sl_curs, GET_WEAPONS)
    for row in weapons_rows:
        weapons_table.append({x:y for x,y in zip(weapons_columns, row)})
        
    return db.armory_weapon.insert_many(weapons_table)


if __name__ == "__main__":
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()
    client = create_mdb_connection(PASSWORD, DBNAME)
    db = client.Module3
    doc_creation_character(db)
    doc_creation_inventory(db)
    doc_creation_items(db)
    doc_creation_weapons(db)

    sl_curs.close()
    sl_conn.close()


