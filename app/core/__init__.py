
from .config import config_init,db_name
config_init()

from .db import DatabaseManager
dm=DatabaseManager()
dm.create_connection()
tables=dm.fetch_query(f'SHOW TABLE STATUS FROM `{db_name}`')
if len(tables)==0:
	dm.execute_query('''CREATE TABLE IF NOT EXISTS user(
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(32) NOT NULL COLLATE 'utf8mb4_general_ci',
    nick VARCHAR(32) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
    verify VARCHAR(32) NOT NULL COLLATE 'utf8mb4_general_ci',
    forgot VARCHAR(32) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
    email VARCHAR(32) NOT NULL COLLATE 'utf8mb4_general_ci',
	time TIMESTAMP NULL DEFAULT (now()),
    PRIMARY KEY (id) USING BTREE,
	UNIQUE INDEX `name` (`name`) USING BTREE);''')
dm.close_connection()

from . import email

print("test core init")

