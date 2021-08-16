# 1. Import the Library 
import sqlite3

# 2. Create a Connection to the Database
conn = sqlite3.connect('rpg_db.sqlite3')

# 3. Open a cursor
cur = conn.cursor()

# 4. Execute Queries
TOTAL_CHARACTERS = cur.execute('SELECT count(*) FROM charactercreator_character;').fetchone()

TOTAL_SUBCLASS = cur.execute('SELECT count(*) FROM charactercreator_necromancer;').fetchone()

TOTAL_ITEMS = cur.execute('SELECT count(*) FROM armory_item;').fetchone()

WEAPONS = cur.execute('SELECT count(*) FROM armory_weapon;').fetchone()

NON_WEAPONS = cur.execute("""SELECT count(item_ptr_id)
                               FROM armory_item
                          LEFT JOIN armory_weapon 
                                 ON armory_item.item_id = armory_weapon.item_ptr_id
                              WHERE armory_weapon.item_ptr_id is NULL;""")

CHARACTER_ITEMS = cur.execute("""SELECT character_id, count(item_id) 
                                   FROM charactercreator_character_inventory 
                               GROUP BY character_id LIMIT 20;""").fetchone()

CHARACTER_WEAPONS = cur.execute("""SELECT character_id, count(item_ptr_id)
                                     FROM armory_weapon
                                LEFT JOIN armory_item 
                                       ON armory_weapon.item_ptr_id = armory_item.item_id
                                     JOIN charactercreator_character_inventory
                                       ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
                                 GROUP BY character_id;""").fetchone()


# note: the variables below bring back an error 'You can only execute one statement at a time.'
AVG_CHARACTER_ITEMS = cur.execute("""SELECT AVG(item_count)
                                       FROM (SELECT COUNT(item_id) as item_count
                                       FROM charactercreator_character_inventory
                                   GROUP BY character_id);;""").fetchone()

AVG_CHARACTER_WEAPONS = cur.execute("""SELECT AVG(weapon_count)
                                     FROM (SELECT COUNT(item_ptr_id) as weapon_count
                                     FROM armory_weapon
                                LEFT JOIN armory_item 
                                       ON armory_weapon.item_ptr_id = armory_item.item_id
                                     JOIN charactercreator_character_inventory
                                       ON armory_weapon.item_ptr_id = charactercreator_character_inventory.item_id
                                 GROUP BY character_id);""").fetchone()



